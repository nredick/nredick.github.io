#!/usr/bin/env python3
"""
Enhanced bibliography import script for Hugo Academic sites.
Extracts more complete bibliographic information and formats citations
in Nature journal style. Automatically copies files and creates proper links.
"""

import re
import os
import sys
import yaml
import argparse
import shutil
from pathlib import Path
from datetime import datetime


def extract_field_value(entry, field_name):
    """Extract field value handling nested braces properly."""
    pattern = rf"{field_name}\s*=\s*\{{"
    match = re.search(pattern, entry, re.IGNORECASE)
    if not match:
        return None

    start_pos = match.end() - 1  # Position of opening brace
    brace_count = 0
    i = start_pos

    while i < len(entry):
        if entry[i] == "{":
            brace_count += 1
        elif entry[i] == "}":
            brace_count -= 1
            if brace_count == 0:
                # Found the matching closing brace
                return entry[start_pos + 1 : i]  # Content between braces
        i += 1

    return None


def parse_bibtex_entry(entry):
    """Parse a single BibTeX entry and extract all fields."""

    # Extract entry type and key
    entry_match = re.match(r"@(\w+)\{([^,]+),", entry)
    if not entry_match:
        return None

    entry_type = entry_match.group(1).lower()
    entry_key = entry_match.group(2)

    # Initialize data structure
    data = {"entry_type": entry_type, "entry_key": entry_key}

    # Define fields to extract
    fields = [
        "title",
        "author",
        "date",
        "journal",
        "journaltitle",
        "volume",
        "number",
        "pages",
        "doi",
        "url",
        "abstract",
        "keywords",
        "eventtitle",
        "venue",
        "type",
        "issn",
        "issue",
        "file",
    ]

    # Extract fields using the improved function
    for field_name in fields:
        value = extract_field_value(entry, field_name)
        if value:
            value = value.strip()
            # Clean up LaTeX formatting more thoroughly
            # Handle multiple nested braces iteratively
            while "{{" in value or "}}" in value:
                old_value = value
                value = re.sub(
                    r"\{\{([^}]*)\}\}", r"\1", value
                )  # Remove double braces {{text}}
                value = re.sub(r"\{\{", "", value)  # Remove orphaned {{
                value = re.sub(r"\}\}", "", value)  # Remove orphaned }}
                if value == old_value:  # Prevent infinite loop
                    break

            value = re.sub(r"\{([^}]+)\}", r"\1", value)  # Remove single braces {text}
            value = value.replace("\\&", "&")  # Fix escaped ampersands
            value = value.replace("\\", "")  # Remove remaining backslashes
            value = " ".join(value.split())  # Normalize whitespace

            # Map journaltitle to journal for consistency
            if field_name == "journaltitle":
                data["journal"] = value
            else:
                data[field_name] = value

    return data


def format_authors(authors_str):
    """Format authors from BibTeX format to list."""
    if not authors_str:
        return []

    # Split by 'and'
    authors = re.split(r"\s+and\s+", authors_str)
    formatted_authors = []

    for author in authors:
        author = author.strip()
        # Handle "Last, First" format
        if "," in author:
            parts = author.split(",", 1)
            last = parts[0].strip()
            first = parts[1].strip()
            formatted_authors.append(f"{first} {last}")
        else:
            formatted_authors.append(author)

    return formatted_authors


def determine_publication_type(entry_type, data):
    """Determine Hugo publication type based on BibTeX entry type and content."""

    type_mapping = {
        "article": "article-journal",
        "inproceedings": "paper-conference",
        "incollection": "chapter",
        "book": "book",
        "phdthesis": "thesis",
        "mastersthesis": "thesis",
        "techreport": "report",
        "unpublished": "manuscript",  # Default for unpublished
    }

    # For unpublished entries, check if it's actually a talk
    if entry_type == "unpublished":
        if (
            data.get("eventtitle")
            or data.get("venue")
            or data.get("type") == "Guest Lecture"
        ):
            return "talk"

    return type_mapping.get(entry_type, "manuscript")


def parse_file_field(file_field):
    """Parse the file field from BibTeX which can contain multiple files."""
    if not file_field:
        return []

    # Split by semicolon for multiple files
    files = []
    parts = file_field.split(";")

    for part in parts:
        part = part.strip()
        if not part:
            continue

        # Handle Zotero-style file paths: /path/to/file.pdf:PDF
        if ":" in part:
            file_path = part.split(":")[0].strip()
        else:
            file_path = part.strip()

        if file_path and Path(file_path).exists():
            files.append(Path(file_path))

    return files


def copy_files_and_create_links(files, entry_dir, entry_key, dry_run=False):
    """Copy files to entry directory and create appropriate links."""
    links = []

    # The directory name should be the Hugo-style name (with hyphens)
    dir_name = entry_key.replace("_", "-").lower()

    for file_path in files:
        if not file_path.exists():
            print(f"Warning: File not found: {file_path}")
            continue

        # Determine file type and create appropriate filename
        suffix = file_path.suffix.lower()

        if suffix == ".pdf":
            # Create a clean filename for PDFs
            new_filename = f"{entry_key.replace('_', '-').lower()}.pdf"
            # Use the actual directory name that exists
            actual_dir_name = entry_dir.name
            link_data = {
                "icon": "fa-file-pdf",
                "url": f"{actual_dir_name}/{new_filename}",
            }
        elif suffix in [".ppt", ".pptx"]:
            new_filename = f"slides{suffix}"
            link_data = {
                "icon": "fa-file-powerpoint",
                "name": "Slides",
                "url": f"{dir_name}/{new_filename}",
            }
        elif suffix in [".doc", ".docx"]:
            new_filename = f"document{suffix}"
            link_data = {
                "icon": "fa-file-word",
                "name": "Document",
                "url": f"{dir_name}/{new_filename}",
            }
        elif suffix in [".xls", ".xlsx"]:
            new_filename = f"data{suffix}"
            link_data = {
                "icon": "fa-file-excel",
                "name": "Data",
                "url": f"{dir_name}/{new_filename}",
            }
        elif suffix in [".zip", ".tar", ".gz"]:
            new_filename = f"supplementary{suffix}"
            link_data = {
                "icon": "fa-file-archive",
                "name": "Supplementary",
                "url": f"{dir_name}/{new_filename}",
            }
        else:
            # For other file types, keep original name
            new_filename = file_path.name
            link_data = {
                "icon": "fa-file",
                "name": "File",
                "url": f"{dir_name}/{new_filename}",
            }

        # Copy the file (or just print what would be copied in dry-run mode)
        dest_path = entry_dir / new_filename
        try:
            if dry_run:
                print(f"[DRY RUN] Would copy: {file_path} -> {dest_path}")
                print(f"[DRY RUN] URL would be: {dir_name}/{new_filename}")
            else:
                shutil.copy2(file_path, dest_path)
                print(f"Copied: {file_path} -> {dest_path}")
            links.append(link_data)
        except Exception as e:
            print(f"Error copying {file_path}: {e}")

    return links


def create_nature_citation_data(data, entry_dir, dry_run=False):
    """Create frontmatter data optimized for Nature-style citations."""

    frontmatter = {
        "title": data.get("title", ""),
        "authors": format_authors(data.get("author", "")),
        "date": data.get("date", ""),
        "publishDate": datetime.now().isoformat() + "Z",
        "publication_types": [determine_publication_type(data["entry_type"], data)],
    }

    # Add journal information
    if data.get("journal"):
        frontmatter["journal"] = data["journal"]

    # Add volume, issue, pages for proper Nature citation
    if data.get("volume"):
        frontmatter["volume"] = data["volume"]

    if data.get("number"):
        frontmatter["issue"] = data["number"]
    elif data.get("issue"):
        frontmatter["issue"] = data["issue"]

    if data.get("pages"):
        frontmatter["pages"] = data["pages"]

    # Add DOI
    if data.get("doi"):
        frontmatter["doi"] = data["doi"]

    # Add abstract
    if data.get("abstract"):
        frontmatter["abstract"] = data["abstract"]

    # Add keywords as tags
    if data.get("keywords"):
        keywords = [k.strip().lower() for k in data["keywords"].split(",")]
        keywords.sort()  # Sort alphabetically
        frontmatter["tags"] = keywords

    # For talks/conferences, add venue information
    if data.get("eventtitle"):
        frontmatter["event"] = data["eventtitle"]

    if data.get("venue"):
        frontmatter["venue"] = data["venue"]

    if data.get("type"):
        frontmatter["talk_type"] = data["type"]

    # Process files and create links
    links = []

    # Handle files from bibliography
    if data.get("file"):
        file_paths = parse_file_field(data["file"])
        file_links = copy_files_and_create_links(
            file_paths, entry_dir, data["entry_key"], dry_run
        )
        links.extend(file_links)

    # Add URL link if present and not a DOI URL
    if data.get("url"):
        url = data["url"]
        # Check if it's a DOI URL (redundant with DOI field)
        if not (
            url.startswith("https://doi.org/") or url.startswith("http://dx.doi.org/")
        ):
            # Determine appropriate icon based on URL
            if "github.com" in url.lower():
                link_data = {"icon": "fa-github", "url": url}
            elif "gitlab.com" in url.lower():
                link_data = {"icon": "fa-gitlab", "name": "GitLab", "url": url}
            elif any(domain in url.lower() for domain in ["youtube.com", "youtu.be"]):
                link_data = {"icon": "fa-youtube", "name": "Video", "url": url}
            elif "slides" in url.lower() or "presentation" in url.lower():
                link_data = {"icon": "fa-file-powerpoint", "name": "Slides", "url": url}
            else:
                link_data = {"url": url}

            links.append(link_data)

    if links:
        frontmatter["links"] = links

    return frontmatter


def parse_bib_file(bib_file):
    """Parse a .bib file and return list of entries."""

    with open(bib_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into individual entries
    entries = re.split(r"\n@", content)
    if entries[0].strip() == "":
        entries = entries[1:]  # Remove empty first element

    # Add @ back to entries (except first)
    for i in range(1, len(entries)):
        entries[i] = "@" + entries[i]

    parsed_entries = []
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue

        # Skip comments
        if entry.startswith("%"):
            continue

        parsed = parse_bibtex_entry(entry)
        if parsed:
            parsed_entries.append(parsed)

    return parsed_entries


def merge_with_existing_content(new_frontmatter, existing_file):
    """Merge new frontmatter with existing file, preserving customizations."""

    if not existing_file.exists():
        return new_frontmatter, ""

    # Read existing file
    with open(existing_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Split frontmatter and content
    parts = content.split("---\n", 2)
    if len(parts) >= 3:
        existing_frontmatter_str = parts[1]
        existing_content = parts[2] if len(parts) > 2 else ""

        try:
            existing_frontmatter = yaml.safe_load(existing_frontmatter_str)
        except yaml.YAMLError:
            print(f"Warning: Could not parse existing frontmatter in {existing_file}")
            existing_frontmatter = {}
    else:
        existing_frontmatter = {}
        existing_content = content

    # Merge frontmatter, preserving existing customizations
    merged_frontmatter = {}

    # Start with new frontmatter as base
    merged_frontmatter.update(new_frontmatter)

    # Preserve certain fields from existing if they exist
    preserve_fields = [
        "links",
        "featured",
        "image",
        "url_pdf",
        "url_code",
        "url_dataset",
        "url_poster",
        "url_project",
        "url_slides",
        "url_source",
        "url_video",
    ]

    for field in preserve_fields:
        if field in existing_frontmatter:
            merged_frontmatter[field] = existing_frontmatter[field]

    # For links specifically, be more careful about merging
    if "links" in existing_frontmatter and "links" in new_frontmatter:
        # Keep existing links, only add new ones if they don't conflict
        existing_links = existing_frontmatter["links"]
        new_links = new_frontmatter["links"]

        # Keep all existing links
        merged_links = existing_links[:]

        # Check what types of links already exist
        existing_icons = {
            link.get("icon") for link in existing_links if link.get("icon")
        }
        existing_urls = {link.get("url") for link in existing_links if link.get("url")}

        # Only add new links that don't duplicate existing functionality
        for new_link in new_links:
            should_add = True

            # Skip if same icon already exists (e.g., don't add second PDF link)
            if new_link.get("icon") and new_link.get("icon") in existing_icons:
                should_add = False

            # Skip if same URL already exists
            if new_link.get("url") and new_link.get("url") in existing_urls:
                should_add = False

            # For DOI links, only add if no DOI link exists
            if new_link.get("name") == "DOI" and any(
                link.get("name") == "DOI" for link in existing_links
            ):
                should_add = False

            if should_add:
                merged_links.append(new_link)

        merged_frontmatter["links"] = merged_links

    return merged_frontmatter, existing_content


def create_content_file(data, output_dir, preserve_existing=True, dry_run=False):
    """Create a Hugo content file from parsed data."""

    # Create output directory
    entry_dir = output_dir / data["entry_key"].replace("_", "-").lower()

    if dry_run:
        print(f"[DRY RUN] Would create directory: {entry_dir}")
    else:
        entry_dir.mkdir(parents=True, exist_ok=True)

    # Create new frontmatter (pass entry_dir for file processing)
    new_frontmatter = create_nature_citation_data(data, entry_dir, dry_run)

    # Check if file exists and merge if preserve_existing is True
    content_file = entry_dir / "index.md"

    if preserve_existing and content_file.exists():
        frontmatter, existing_content = merge_with_existing_content(
            new_frontmatter, content_file
        )
        action = "Updated (preserving customizations)"
    else:
        frontmatter = new_frontmatter
        existing_content = ""
        action = "Created"

    if dry_run:
        print(f"\n[DRY RUN] {action}: {content_file}")
        print("=" * 60)
        print("---")
        print(
            yaml.dump(
                frontmatter,
                default_flow_style=False,
                allow_unicode=True,
                width=float("inf"),
            ),
            end="",
        )
        print("---")
        if existing_content:
            print(existing_content)
        print("=" * 60)
    else:
        # Write the file
        with open(content_file, "w", encoding="utf-8") as f:
            f.write("---\n")
            yaml.dump(
                frontmatter,
                f,
                default_flow_style=False,
                allow_unicode=True,
                width=float("inf"),
            )
            f.write("---\n")
            if existing_content:
                f.write(existing_content)
        print(f"{action}: {content_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Enhanced bibliography import for Hugo Academic"
    )
    parser.add_argument("bib_file", help="Input .bib file")
    parser.add_argument("output_dir", help="Output directory for content files")
    parser.add_argument(
        "--overwrite", action="store_true", help="Completely overwrite existing files"
    )
    parser.add_argument(
        "--preserve",
        action="store_true",
        default=True,
        help="Preserve existing customizations (default)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )

    args = parser.parse_args()

    bib_file = Path(args.bib_file)
    output_dir = Path(args.output_dir)

    if not bib_file.exists():
        print(f"Error: {bib_file} does not exist")
        sys.exit(1)

    if args.dry_run:
        print("=== DRY RUN MODE ===")
        print("No files will be created or modified")
        print()

    # Parse the .bib file
    print(f"Parsing {bib_file}...")
    entries = parse_bib_file(bib_file)

    print(f"Found {len(entries)} entries")

    # Create content files
    for entry in entries:
        entry_dir = output_dir / entry["entry_key"].replace("_", "-").lower()

        if (
            entry_dir.exists()
            and not args.overwrite
            and not args.preserve
            and not args.dry_run
        ):
            print(
                f"Skipping {entry['entry_key']} (already exists, use --overwrite to replace)"
            )
            continue

        # If overwrite is True, don't preserve existing content
        preserve_existing = not args.overwrite
        create_content_file(entry, output_dir, preserve_existing, args.dry_run)


if __name__ == "__main__":
    main()
