import os
import requests
import hashlib
import random
import string

# Function to generate a 10-character random code
def generate_random_code():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return code

# Function to generate the code and hide it in multiple folders
def generate_and_hide_code():
    code = generate_random_code()  # Generate random code
    with open("hwop.txt", "w") as file:
        file.write(code)

    folders = [generate_random_code() for _ in range(5)]  # Generate 5 random folder names
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        os.rename("hwop.txt", os.path.join(folder, "hwop.txt"))
    
    return code

# Function to verify the code with the provided Pastebin raw URL
def verify_code(pastebin_raw_url, generated_code):
    response = requests.get(pastebin_raw_url)
    remote_code = response.text.strip()

    if remote_code == generated_code:
        print("Hello, world!")
    else:
        print("The generated code is:", generated_code)
        print("You are not allowed to use it.")

# Main function
def main():
    generated_code = generate_and_hide_code()
    pastebin_raw_url = "https://pastebin.com/raw/3e5jh1Qj"  # Replace with your Pastebin raw URL
    verify_code(pastebin_raw_url, generated_code)

if __name__ == "__main__":
    main()
