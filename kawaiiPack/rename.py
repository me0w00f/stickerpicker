import os
import random
import string
import time

# Define the directory to monitor and file name to look for
directory_to_monitor = "."  # Current directory, change as necessary
file_to_monitor = input("Filename: __")

# Function to generate a random 5 character string
def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to monitor and rename file if it exists
def monitor_and_rename():
    # Monitor the directory indefinitely
    while True:
        # Check if the specified file exists in the directory
        if file_to_monitor in os.listdir(directory_to_monitor):
            # Generate a new random name
            new_name = generate_random_string() + ".webp"
            # Form the full old and new file paths
            old_file = os.path.join(directory_to_monitor, file_to_monitor)
            new_file = os.path.join(directory_to_monitor, new_name)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed {file_to_monitor} to {new_name}")
        
        # Wait for a short period before checking again
        time.sleep(2)  # checks every 2 seconds

# Call the function to start monitoring
print(f"Monitoring for '{file_to_monitor}' in '{directory_to_monitor}'...")
monitor_and_rename()
