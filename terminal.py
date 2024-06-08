import os
import requests

# Function to fetch the current Codespace URL
def get_codespace_url():
    # Simulate fetching the URL, replace this with the actual method to obtain the Codespace URL
    # For example, we assume it's stored in an environment variable CODESPACE_URL
    codespace_url = os.getenv('CODESPACE_URL')
    
    if not codespace_url:
        # For the sake of this example, we assume the URL is stored in a local file
        try:
            with open('/path/to/codespace_url.txt', 'r') as file:
                codespace_url = file.read().strip()
        except FileNotFoundError:
            pass
    
    return codespace_url

# Pastebin raw URL containing the allowed URLs
pastebin_raw_url = 'https://pastebin.com/raw/UHkWyd4e'

def check_url_in_pastebin(codespace_url, pastebin_raw_url):
    try:
        # Fetch content from Pastebin
        response = requests.get(pastebin_raw_url)
        response.raise_for_status()
        
        # Get the list of allowed URLs from Pastebin content
        allowed_urls = response.text.splitlines()
        
        # Check if the Codespace URL is in the allowed URLs
        if codespace_url in allowed_urls:
            print("Hello World")
        else:
            print("You are not allowed to use it")
    except requests.RequestException as e:
        print(f"Error fetching Pastebin content: {e}")

if __name__ == "__main__":
    # Fetch the Codespace URL
    codespace_url = get_codespace_url()
    
    if codespace_url:
        check_url_in_pastebin(codespace_url, pastebin_raw_url)
    else:
        print("Codespace URL could not be obtained")
      
