#!/usr/bin/env python3
"""
Generate llms.txt and llms-full.txt for developer.seatable.com.

Reads the nav structure from mkdocs.yml and produces:
  - docs/llms.txt       (compact overview with links)
  - docs/llms-full.txt  (full markdown content of all pages)

Usage:
  python3 scripts/generate_llms_txt.py
"""

import os
import re
import sys

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(REPO_ROOT, "docs")
MKDOCS_YML = os.path.join(REPO_ROOT, "mkdocs.yml")
BASE_URL = "https://developer.seatable.com"

# Files to skip (fragments, includes, non-content)
SKIP_FILES = {"includes.md"}


def load_mkdocs_config():
    # Custom loader that ignores !!python/name: and !!python/object: tags
    # which mkdocs.yml uses for plugins/extensions
    loader = yaml.SafeLoader
    loader.add_multi_constructor(
        "tag:yaml.org,2002:python/",
        lambda loader, suffix, node: None,
    )
    with open(MKDOCS_YML, "r") as f:
        return yaml.load(f, Loader=loader)


def extract_nav_pages(nav, section_path=""):
    """Recursively extract (section, title, md_path) tuples from the nav."""
    pages = []
    for item in nav:
        if isinstance(item, str):
            # Bare path like "ruby/index.md"
            pages.append((section_path, "", item))
        elif isinstance(item, dict):
            for title, value in item.items():
                if isinstance(value, str):
                    # "Ruby: ruby/index.md" — top-level single-page section
                    # Use title as section if no parent section
                    section = section_path or title
                    pages.append((section, title, value))
                elif isinstance(value, list):
                    # Nested section
                    pages.extend(extract_nav_pages(value, section_path=title))
    return pages


def md_path_to_url(md_path):
    """Convert a docs-relative markdown path to a site URL."""
    # index.md -> /
    # python/index.md -> /python/
    # python/objects/metadata.md -> /python/objects/metadata/
    url_path = md_path.replace(".md", "/")
    if url_path.endswith("index/"):
        url_path = url_path[: -len("index/")]
    return f"{BASE_URL}/{url_path}"


def read_md_file(md_path):
    """Read a markdown file from the docs directory, return its content."""
    full_path = os.path.join(DOCS_DIR, md_path)
    if not os.path.exists(full_path):
        print(f"Warning: {full_path} not found, skipping", file=sys.stderr)
        return None
    with open(full_path, "r") as f:
        return f.read()


def clean_for_llm(content):
    """Remove MkDocs-specific syntax that adds noise for LLMs."""
    # Remove include-markdown directives
    content = re.sub(
        r"\{%\s*include-markdown\s+.*?%\}", "", content, flags=re.DOTALL
    )
    # Remove admonition-style blocks but keep their content
    # e.g., !!! tip "Title"\n\n    Content -> Content
    content = re.sub(r"^!!! \w+.*$", "", content, flags=re.MULTILINE)
    # Remove HTML comments
    content = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
    # Remove style blocks
    content = re.sub(r"<style>.*?</style>", "", content, flags=re.DOTALL)
    # Collapse 3+ blank lines to 2
    content = re.sub(r"\n{3,}", "\n\n", content)
    return content.strip()


# ---------------------------------------------------------------------------
# llms.txt (compact index)
# ---------------------------------------------------------------------------
def generate_llms_txt(config, nav_pages):
    site_name = config.get("site_name", "SeaTable Developer Manual")
    site_desc = config.get("site_description", "").strip()

    lines = [
        f"# {site_name}",
        "",
        f"> {site_desc}",
        "",
    ]

    # Group pages by section
    sections = {}
    for section, title, md_path in nav_pages:
        if os.path.basename(md_path) in SKIP_FILES:
            continue
        sections.setdefault(section or "Introduction", []).append((title, md_path))

    lines.append("## Sections")
    lines.append("")

    for section, pages in sections.items():
        lines.append(f"### {section}")
        lines.append("")
        for title, md_path in pages:
            url = md_path_to_url(md_path)
            label = title or section
            lines.append(f"- [{label}]({url})")
        lines.append("")

    lines += [
        "## Complete Content",
        "",
        f"- [llms-full.txt]({BASE_URL}/llms-full.txt):"
        " Complete developer manual with all pages, code examples, and API references",
        "",
        "## Optional",
        "",
        "- [SeaTable Website](https://seatable.com): Product website with features, pricing, and use cases",
        "- [REST API Reference](https://api.seatable.com): Interactive REST API documentation with all endpoints",
        "- [Admin Manual](https://admin.seatable.com): Self-hosting installation, configuration, and administration",
        "- [Community Forum](https://forum.seatable.com): Community support, discussions, and feature requests",
    ]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# llms-full.txt (complete content)
# ---------------------------------------------------------------------------
def generate_llms_full_txt(config, nav_pages):
    site_name = config.get("site_name", "SeaTable Developer Manual")
    site_desc = config.get("site_description", "").strip()

    lines = [
        f"# {site_name}",
        "",
        f"{site_desc}",
        "",
        f"Base URL: {BASE_URL}",
        "",
    ]

    current_section = None
    for section, title, md_path in nav_pages:
        if os.path.basename(md_path) in SKIP_FILES:
            continue

        content = read_md_file(md_path)
        if content is None:
            continue

        content = clean_for_llm(content)

        # Section header
        if section and section != current_section:
            lines += [f"## {section}", ""]
            current_section = section

        # Page content
        url = md_path_to_url(md_path)
        lines.append(f"Source: {url}")
        lines.append("")
        lines.append(content)
        lines += ["", "---", ""]

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    config = load_mkdocs_config()
    nav = config.get("nav", [])
    nav_pages = extract_nav_pages(nav)

    llms_txt = generate_llms_txt(config, nav_pages)
    llms_txt_path = os.path.join(DOCS_DIR, "llms.txt")
    with open(llms_txt_path, "w") as f:
        f.write(llms_txt)
    print(f"llms.txt      — {len(llms_txt):,} bytes, {len(nav_pages)} pages")

    llms_full = generate_llms_full_txt(config, nav_pages)
    llms_full_path = os.path.join(DOCS_DIR, "llms-full.txt")
    with open(llms_full_path, "w") as f:
        f.write(llms_full)
    print(f"llms-full.txt — {len(llms_full):,} bytes")


if __name__ == "__main__":
    main()
