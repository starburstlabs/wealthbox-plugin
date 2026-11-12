#!/usr/bin/env python3
"""Validate and package the Wealthbox conversational MCP plugin using Python 3."""

import argparse
import json
from pathlib import Path
import re
import shutil
import tempfile
from urllib.parse import urlsplit
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


UI_TOOLS = (
    "OpenWealthbox", "ShowContactCard", "ShowClientMeetingBrief",
    "PreviewMeetingFollowUp", "SaveApprovedMeetingFollowUp",
    "SearchContactMentions",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def source_files(repository):
    """Map shared and OpenAI-only source to paths inside the generated package."""
    repository = repository.resolve()
    files = {}

    def add(source, target):
        require(target not in files, f"Duplicate package path: {target}")
        require(source.is_file() and not source.is_symlink(), f"Missing source file or symlink: {source}")
        require(source.resolve().is_relative_to(repository), f"Source escapes the repository: {source}")
        files[target] = source

    for name in ("plugin.json", "mcp.json", "README.md", "CHATGPT-REVIEW.md"):
        add(repository / "openai" / name, Path(name))
    add(repository / "LICENSE", Path("LICENSE"))
    for source_root, target_root in (
        (repository / "skills", Path("skills")),
        (repository / "openai/skills", Path("skills")),
        (repository / "assets", Path("assets")),
    ):
        for path in source_root.rglob("*"):
            require(not path.is_symlink(), f"Source cannot contain symlinks: {path}")
            if path.is_file():
                add(path, target_root / path.relative_to(source_root))
    return files


def package_files(root):
    manifest = read_json(root / "plugin.json")
    require(manifest.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            "plugin.json must use the portable Agent Plugins schema")
    require(re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")), "Version must use SemVer")
    extension = manifest.get("extensions", {}).get("com.openai", {})
    require(not manifest.get("apps") and not extension.get("apps"), "Public package cannot bind a private App")
    require(not manifest.get("hooks") and not extension.get("hooks"), "Public package cannot declare hooks")
    interface = extension["interface"]
    require(0 < len(interface["shortDescription"]) <= 30, "Subtitle must be 1-30 characters")
    require(interface["capabilities"] == ["Read", "Write"], "Capabilities must describe conversational CRM tools")
    for field in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        require(urlsplit(interface[field]).scheme == "https", f"{field} must use HTTPS")
    for field in ("logo", "composerIcon"):
        asset = (root / interface[field]).resolve()
        require(asset.is_relative_to(root) and asset.is_file(), f"Missing or external asset: {field}")

    configuration = read_json(root / "mcp.json")
    require(configuration.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
            "mcp.json must use the portable MCP schema")
    servers = configuration["mcpServers"]
    require(set(servers) == {"wealthbox"}, "Expected the Wealthbox MCP connection")
    server = servers["wealthbox"]
    require(server.get("type") == "streamable-http", "Expected remote HTTP transport")
    require(server.get("url") == "https://mcp.crmworkspace.com/mcp", "Expected the production MCP endpoint")
    require(not server.get("headers"), "Do not package credential headers")
    auth = server["extensions"]["com.openai"]["auth"]
    require(auth.get("type") == "oauth", "Expected OAuth")
    require(set(auth.get("baseScopes", [])) == {"mcp:read", "mcp:write"}, "Unexpected OAuth scopes")

    skills = sorted((root / "skills").glob("*/SKILL.md"))
    require(len(skills) == 6, "Expected all six Wealthbox skills")
    for skill in skills:
        text = skill.read_text(encoding="utf-8")
        require(text.startswith("---\n") and "\n---\n" in text[4:], f"Missing frontmatter: {skill}")
        frontmatter = text.split("---\n", 2)[1]
        require(re.search(rf"^name: {re.escape(skill.parent.name)}$", frontmatter, re.M),
                f"Skill name does not match its directory: {skill}")
        require(re.search(r"^description:\s*\S", frontmatter, re.M), f"Missing skill description: {skill}")

    files = [root / name for name in ("plugin.json", "mcp.json", "README.md", "LICENSE", "CHATGPT-REVIEW.md")]
    for directory in ("skills", "assets"):
        files.extend(path for path in (root / directory).rglob("*") if path.is_file())
    for path in files:
        require(path.is_file() and not path.is_symlink(), f"Missing file or symlink: {path}")
        require(path.resolve().is_relative_to(root), f"File escapes the package: {path}")
        if path.suffix == ".md" and "skills" in path.relative_to(root).parts:
            text = path.read_text(encoding="utf-8")
            require(not any(name in text for name in UI_TOOLS), f"Skill references a UI-only tool: {path}")
    return sorted(files), len(skills)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, nargs="?", help="ZIP destination; defaults to dist/wealthbox-openai.zip")
    arguments = parser.parse_args()
    repository = Path(__file__).resolve().parents[1]
    distribution = repository / "dist"
    root = distribution / "openai/wealthbox"
    output = arguments.output.resolve() if arguments.output else distribution / "wealthbox-openai.zip"
    require(not output.is_relative_to(repository) or output.is_relative_to(distribution),
            "Write the archive outside the source tree or under dist/")
    require(not output.is_relative_to(root), "Write the archive outside the generated plugin directory")
    require(output.suffix == ".zip", "Archive destination must end in .zip")
    sources = source_files(repository)
    distribution.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="openai-", dir=distribution) as temporary:
        staging = Path(temporary)
        for target, source in sources.items():
            destination = staging / target
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
        files, skill_count = package_files(staging)
        output.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
            for path in files:
                entry = ZipInfo(path.relative_to(staging).as_posix(), date_time=(1980, 1, 1, 0, 0, 0))
                entry.compress_type = ZIP_DEFLATED
                entry.external_attr = 0o100644 << 16
                archive.writestr(entry, path.read_bytes())
        if root.exists():
            shutil.rmtree(root)
        shutil.copytree(staging, root)
    with ZipFile(output) as archive:
        require(archive.testzip() is None, "Archive integrity check failed")
        require(json.loads(archive.read("plugin.json")) == read_json(root / "plugin.json"),
                "Archive manifest differs from source")
    print(f"Built {output}: {len(files)} files, {skill_count} skills, production OAuth MCP connection")
    print(f"Plugin directory: {root}")
    print("Production catalog, host behavior and submission materials require separate checks.")


if __name__ == "__main__":
    try:
        main()
    except (KeyError, ValueError) as error:
        raise SystemExit(f"Package validation failed: {error}") from error
