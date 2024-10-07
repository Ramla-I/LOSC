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

# Find all files in the folder, search for the specific strings and count the occurrences
count_ensures=$(grep -roh "#\[ensures" "$FOLDER" | wc -l)
count_requires=$(grep -roh "#\[requires" "$FOLDER" | wc -l)
count_extern=$(grep -roh "#\[extern_spec" "$FOLDER" | wc -l)
count_trusted=$(grep -roh "#\[trusted\]" "$FOLDER" | wc -l)
count_pure=$(grep -roh "#\[pure\]" "$FOLDER" | wc -l)
count_verified=$(grep -roh "#\[verified\]" "$FOLDER" | wc -l)
count_type_invariant=$(grep -roh "#\[invariant" "$FOLDER" | wc -l)
count_body_invariant=$(grep -roh "body_invariant!(" "$FOLDER" | wc -l)

# Sum all counts
total_count=$((count_ensures + count_requires + count_extern + count_trusted + count_pure + count_verified + count_type_invariant))

# Display the results
echo "Occurrences of the following tags in the folder '$FOLDER':"
echo "--------------------------------------------"
echo "#[ensures]       : $count_ensures"
echo "#[requires]      : $count_requires"
echo "#[extern_spec]   : $count_extern"
echo "#[trusted]       : $count_trusted"
echo "#[pure]          : $count_pure"
echo "#[verified]      : $count_verified"
echo "#[invariant]     : $count_type_invariant"
echo "--------------------------------------------"
echo "Total Spec LOC   : $total_count"

echo "Total Proof LOC  : $count_body_invariant"