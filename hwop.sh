#!/bin/bash

# Function to generate a 10-character random code
generate_random_code() {
    cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1
}

# Function to generate the code and hide it in multiple folders
generate_and_hide_code() {
    code=$(generate_random_code)
    mkdir code_folder
    mkdir code_folder/sub_folder
    echo "$code" > code_folder/sub_folder/hwop.txt

    for i in {1..5}; do
        folder_name=$(generate_random_code)
        mkdir "$folder_name"
        cp code_folder/sub_folder/hwop.txt "$folder_name/hwop.txt"
    done
}

# Function to verify the code with the provided Pastebin raw URL
verify_code() {
    remote_code=$(curl -s "$1")
    local_code=$(cat code_folder/sub_folder/hwop.txt)

    if [ "$remote_code" == "$local_code" ]; then
        echo "Hello, world!"
    else
        echo "The generated code is: $local_code"
        echo "You are not allowed to use it."
    fi
}

# Main function
main() {
    generate_and_hide_code
    pastebin_raw_url="https://pastebin.com/raw/3e5jh1Qj"  # Replace with your Pastebin raw URL
    verify_code "$pastebin_raw_url"
}

main
