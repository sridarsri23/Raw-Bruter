markdown

# Brute-Force Login Script with Progress Tracking

This script performs a brute-force attack to attempt logins using a list of usernames and passwords on a specified target URL. The script utilizes `curl` with Digest Authentication and provides a progress bar to track the progress of the attempts. It also saves progress to a file to allow resuming from the last attempt in case of interruption.

## Prerequisites

- Python 3.x
- `curl` installed on your system
- A target URL that supports Digest Authentication

## Usage

1. **Prepare the wordlists:**

   - Create a file named `user.txt` containing the usernames, one per line.
   - Ensure the password wordlist is available at `/usr/share/seclists/Passwords/xato-net-10-million-passwords-100000.txt`.

2. **Set the target URL:**

   Edit the `url` variable in the script to point to the target URL.

   ```python
   url = "http://123.231.93.157:5400"

    Run the script:

    Execute the script using Python:

    bash

    python brute_force.py

    The script will display a progress bar indicating the number of attempts made and the estimated time left. If a valid username and password combination is found, it will print the success message and stop further attempts.

Script Details
Functions

    attempt_login(username, password):
    Attempts a login using the provided username and password. Returns True if the login is successful (HTTP status code 200), otherwise returns False.

    save_progress(username, password):
    Saves the current progress to a file named progress.txt.

    load_progress():
    Loads the progress from the progress.txt file, if it exists.

Progress Tracking

The script saves the current username and password being tried to progress.txt. This allows the script to resume from the last attempt in case it is interrupted.
Dependencies

    subprocess: Used to execute the curl command.
    time: Used to track the start time and calculate the estimated time left.
    tqdm: Used to display the progress bar.
    os: Used to check if the progress file exists and to remove it upon successful login.

Example Output

yaml

Brute-forcing:  50%|█████████████████████████████▌                        | 50000/100000 [00:30<00:30, 1632.47 attempt/s, ETA: 30.64 sec]
Success! Username: admin, Password: password123

License

This project is licensed under the MIT License. See the LICENSE file for details.

sql


Feel free to customize the `README.md` file as needed to match your specific requirements and environment.

mention requirements must satisfied, how to install those and network breakdown features..
ChatGPT

Sure, here's an updated README.md with the additional sections for requirements, installation, and network breakdown features:

markdown

# Brute-Force Login Script with Progress Tracking

This script performs a brute-force attack to attempt logins using a list of usernames and passwords on a specified target URL. The script utilizes `curl` with Digest Authentication and provides a progress bar to track the progress of the attempts. It also saves progress to a file to allow resuming from the last attempt in case of interruption.

## Prerequisites

- Python 3.x
- `curl` installed on your system
- A target URL that supports Digest Authentication

## Installation

1. **Install Python 3.x:**

   - For Ubuntu/Debian:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

   - For CentOS/RHEL:
     ```bash
     sudo yum install python3 python3-pip
     ```

   - For Windows:
     Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install `curl`:**

   - For Ubuntu/Debian:
     ```bash
     sudo apt update
     sudo apt install curl
     ```

   - For CentOS/RHEL:
     ```bash
     sudo yum install curl
     ```

   - For Windows:
     Download and install curl from [curl.se](https://curl.se/windows/).

3. **Install Python dependencies:**

   - Using `pip`:
     ```bash
     pip3 install tqdm
     ```

## Usage

1. **Prepare the wordlists:**

   - Create a file named `user.txt` containing the usernames, one per line.
   - Ensure the password wordlist is available at `/usr/share/seclists/Passwords/xato-net-10-million-passwords-100000.txt`.

2. **Set the target URL:**

   Edit the `url` variable in the script to point to the target URL.

   ```python
   url = "http://123.231.93.157:5400"

    Run the script:

    Execute the script using Python:

    bash

    python brute_force.py

    The script will display a progress bar indicating the number of attempts made and the estimated time left. If a valid username and password combination is found, it will print the success message and stop further attempts.

Script Details
Functions

    attempt_login(username, password):
    Attempts a login using the provided username and password. Returns True if the login is successful (HTTP status code 200), otherwise returns False.

    save_progress(username, password):
    Saves the current progress to a file named progress.txt.

    load_progress():
    Loads the progress from the progress.txt file, if it exists.

Progress Tracking

The script saves the current username and password being tried to progress.txt. This allows the script to resume from the last attempt in case it is interrupted.
Dependencies

    subprocess: Used to execute the curl command.
    time: Used to track the start time and calculate the estimated time left.
    tqdm: Used to display the progress bar.
    os: Used to check if the progress file exists and to remove it upon successful login.

Network Breakdown Features

    Digest Authentication:
    The script uses Digest Authentication for secure login attempts, ensuring that passwords are not sent in plain text over the network.

    HTTP Status Codes:
        200: Indicates a successful login.
        403: Indicates that the login attempt was blocked.
        Other codes: Indicate various other responses from the server, but are not explicitly handled in this script.

    Progress Saving:
    The script saves the last attempted username and password to progress.txt to allow resuming from the point of interruption.

Example Output

yaml

Brute-forcing:  50%|█████████████████████████████▌                        | 50000/100000 [00:30<00:30, 1632.47 attempt/s, ETA: 30.64 sec]
Success! Username: admin, Password: password123

License

This project is licensed under the MIT License. See the LICENSE file for details.

css


This `README.md` now includes sections on requirements, how to install those requirements, and a breakdown of the network-related features of the script.

