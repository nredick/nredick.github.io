#!/bin/sh

cd ..

if [ "$1" == "--overwrite" ]; then
    echo "Overwriting existing entries"
    academic import papers.bib content/papers/ --compact --verbose --normalize --overwrite
    academic import talks.bib content/talks/ --compact --verbose --normalize --overwrite
else
    academic import papers.bib content/papers/ --compact --verbose --normalize
    academic import talks.bib content/talks/ --compact --verbose --normalize
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
