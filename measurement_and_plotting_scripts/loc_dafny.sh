#!/bin/bash

# Check if folder is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 folder_path"
  exit 1
fi

# Folder to search in
FOLDER="$1"

# # Ensure the folder exists
# if [ ! -d "$FOLDER" ]; then
#   echo "Error: Folder '$FOLDER' does not exist."
#   exit 1
# fi

# Initialize line count
total_lines=0

# Find all .dfy files and count non-empty and non-comment lines
for file in $(find "$FOLDER" -name "*.dfy"); do
  lines_in_file=$(grep -v '^\s*$' "$file" | grep -v '^\s*//' | wc -l)
  total_lines=$((total_lines + lines_in_file))
done

# Output the total line count
echo "Total lines of code (LOC) in Dafny files in '$FOLDER': $total_lines"
