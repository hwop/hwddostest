import os
import requests
import pyperclip
import random
import string

# Generate a random directory name
def generate_directory_name(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Generate a random 10-digit code
def generate_code():
    code = ''.join(str(random.randint(0, 9)) for _ in range(10))
    directory = generate_directory_name()
    nested_dirs = os.path.join(*[generate_directory_name() for _ in range(1000)])
    os.makedirs(os.path.join(directory, nested_dirs), exist_ok=True)
    filepath = os.path.join(directory, nested_dirs, "hwop.txt")
    with open(filepath, "w") as file:
        file.write(code)
    return code

# Read code from file
def read_code():
    directory = os.path.join(os.path.expanduser('~'), generate_directory_name())
    nested_dirs = os.path.join(*[generate_directory_name() for _ in range(1000)])
    filepath = os.path.join(directory, nested_dirs, "hwop.txt")
    try:
        with open(filepath, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

# Get code from Pastebin raw
def get_code_from_pastebin(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

# Check if provided code matches the saved one
def check_code(provided_code, saved_code):
    return provided_code == saved_code

def main():
    try:
        # Try to read the saved code
        saved_code = read_code()
    except FileNotFoundError:
        # If the file doesn't exist, generate a new code
        saved_code = generate_code()

    # Copy the code to clipboard
    pyperclip.copy(saved_code)
    print("Code copied to clipboard:", saved_code)

    # Get the Pastebin raw link from the user
    pastebin_url = input("Please enter the Pastebin raw link containing the code: ")

    # Get the code from Pastebin raw
    provided_code = get_code_from_pastebin(pastebin_url)

    # Check if the provided code matches the saved one
    if provided_code and check_code(provided_code, saved_code):
        print("Hello, world!")
    else:
        print("You are not allowed to use it.")

if __name__ == "__main__":
    main()
