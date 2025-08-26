#!/bin/bash
for file in *.txt
do
    if [ -f "$file" ]; then
    file1 = "$file.txt"
    new_file = "${file1}.bak"
    mv "$file" "$new_file"

    fi

done
##################################
#!/bin/bash
read -p "please enter file's name: ", file_name
if [ ! -f "file_name" ]; then
    touch "$file_name"
else
    number_lines=

fi
##################################
#!/bin/bash
read -p "pleas enter file's name: ", file_name
read -p "pleas enter string: ", string
if [] then

fi

