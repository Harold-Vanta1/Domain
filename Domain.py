import socket


domain = input("Domain : ").lower()

# Remove unwanted characters from the domain name
domain = domain.strip("http://").strip("https://").strip("www.").strip()

# Get the top-level domain (TLD) of the domain name
tld = domain.split(".")[-1]
# Use a dictionary to store the mapping between TLDs and whois servers
whois_servers = {
    "org": "whois.pir.org",
    "com": "whois.verisign-grs.com",
    "net": "whois.verisign-grs.com",
    # Add more TLDs and whois servers as needed
}

# Get the whois server for the TLD, or use a default value if not found
whois_server = whois_servers.get(tld, "whois.iana.org")

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Use a try-except block to handle any errors
try:
    # Connect to the whois server on port 43
    s.connect((whois_server, 43))
    # Send the domain name followed by a carriage return and a newline
    s.send((domain + "\r\n").encode())
    # Initialize an empty bytes object to store the received data
    msg = b""
    # Use a while loop to receive all the data until the socket is closed
    while True:
        # Receive up to 4096 bytes of data at a time
        data = s.recv(4096)
        # If no data is received, break the loop
        if not data:
            break
        # Append the received data to the msg object
        msg += data
    # Close the socket
    s.close()
    # Decode the bytes object to a string using utf-8 encoding
    msg = msg.decode("utf-8")
    # Print the whois information
    print(msg)
except socket.error as e:
    # Print the socket error
    print("Socket error:", e)
