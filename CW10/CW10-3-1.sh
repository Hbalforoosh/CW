#!/bin/bash
for file in *.txt
do
    if [ -f "$file" ]; then
    file1="$file.txt"
    new_file="${file1}.bak"
    mv "$file" "$new_file"

    fi

done