#!/bin/sh

cd ..

# Use enhanced Python import script for better Nature-style formatting
if [ "$1" == "--overwrite" ]; then
    echo "Completely overwriting existing entries with enhanced import"
    python3 scripts/enhanced_import.py papers.bib content/papers/ --overwrite
    python3 scripts/enhanced_import.py talks.bib content/talks/ --overwrite
elif [ "$1" == "--dry-run" ]; then
    echo "DRY RUN: Showing what would be imported without making changes"
    python3 scripts/enhanced_import.py papers.bib content/papers/ --dry-run
    python3 scripts/enhanced_import.py talks.bib content/talks/ --dry-run
else
    echo "Importing with enhanced script (preserving existing customizations)"
    python3 scripts/enhanced_import.py papers.bib content/papers/ --preserve
    python3 scripts/enhanced_import.py talks.bib content/talks/ --preserve
fi

# Loop over all .md files in this directory and all subdirectories
find content/talks/ -type f -name "*.md" | while read -r file; do
    # Check if the file contains "publication_types:"
    if grep -q "publication_types:" "$file" && grep -q "manuscript" "$file"; then
        echo "Updating $file manuscript type"

        # Use sed to replace 'manuscript' with 'talk' in the YAML front matter
        sed -i '' -e '/^publication_types:/,/^---/{
            /- manuscript/{
                s/- manuscript/- talk/
            }
        }' "$file"
    fi

    if grep -q "doi:" "$file" && grep -q "coi" "$file"; then
        echo "Updating $file doi"

        # Use sed to replace 'manuscript' with 'talk' in the YAML front matter
        sed -i '' -e '/^publication_types:/,/^---/{
            /- manuscript/{
                s/- manuscript/- talk/
            }
        }' "$file"
    fi
done

# hugoblox:
#   ids:
#     doi:
