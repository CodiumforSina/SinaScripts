
DoS Attack Script

This script is designed to perform a Denial of Service (DoS) attack on a specified URL by flooding it with HTTP requests on a chosen port. It utilizes the `socket`, `subprocess`, and `os` modules in Python.

Usage

1. Ping Callback Function (`callback`):
   - This function performs a ping to the specified URL to retrieve its IP address.
   - It prompts the user to enter a port number and establishes a connection to that port.
   - It then sends a series of HTTP requests to the connected port to simulate a DoS attack.

2. Port Reset Function (`reset_port`):
   - Similar to the `callback` function, this function resets the port and performs a DoS attack on the new port.

3. Main Execution Function (`run`):
   - Executes a DoS attack on the specified URL and port.

Instructions

1. Run the script and provide a random URL when prompted.
2. Enter a port number to initiate the DoS attack.
3. Monitor the output to see the progress of the attack.
4. The script will indicate whether the attack was successful or not.

Note
- It's important to use this script responsibly and only on systems and networks that you have explicit permission to test.

