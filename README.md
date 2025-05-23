# **Domain**
This code is a Python program that uses sockets to query the whois information of any domain name entered by the user. Here is a line-by-line explanation of what the code does:
- The first line imports the socket module, which provides access to the low-level network interface in Python.
- The second line asks the user to enter a domain name, such as [python.org](https://www.python.org/), and converts it to lowercase.
  
![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)


## **Cleaning the domain name**
```python
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

```
- The next four lines remove any unwanted characters from the domain name, such as `http://`, `https://`, or `www.`, which are not part of the domain name itself.
- The next line splits the domain name by the dot (`.`) character and takes the last element, which is the top-level domain (TLD) of the domain name, such as `org`, `com`, or `net`.
## **Defining the whois server dictionary**
- The next six lines define a dictionary that maps some common TLDs to their corresponding whois servers, which are the servers that store the whois information for those domains. For example, the whois server for `org` domains is `whois.pir.org`, and the whois server for `com` and `net` domains is `whois.verisign-grs.com`. The dictionary also has a default value of `whois.iana.org`, which is the whois server for the Internet Assigned Numbers Authority (IANA).
- The next line uses the `get` method of the dictionary to find the whois server for the given TLD, or use the default value if the TLD is not in the dictionary.

## **Screenshot of the code**

![Screenshot 2024-02-27 002852](https://github.com/user-attachments/assets/80e8a220-7fb7-4c62-bcc9-f3126cfd50d8)



## **Creating a socket object**
- The next line creates a socket object, which is an endpoint of a network communication. The socket object is initialized with two parameters: `socket.AF_INET` and `socket.SOCK_STREAM`. The first parameter specifies the address family of the       socket, which is `AF_INET` for IPv4 addresses. The second parameter specifies the socket type, which is `SOCK_STREAM` for TCP sockets.
   ## **Handling socket errors**
- The next four lines use a try-except block to handle any errors that may occur during the socket operation. The try block contains the code that performs the socket communication, and the except block handles the `socket.error` exception, which   is raised when a socket error occurs.
- The first line in the try block uses the `connect` method of the socket object to establish a connection to the whois server on port 43, which is the standard port for whois protocol. The `connect` method takes a tuple as an argument, which       contains the host name and the port number of the server.
   ## **Creating a socket object**
- The next line uses the `send` method of the socket object to send the domain name to the whois server, followed by a carriage return (`\r`) and a newline (`\n`) characters, which indicate the end of the request. The `send` method takes a bytes    object as an argument, so the domain name is encoded using utf-8 encoding before sending.
- The next line initializes an empty bytes object, which will store the received data from the whois server.
- The next five lines use a while loop to receive all the data from the whois server until the socket is closed. The loop condition is `True`, which means it will run indefinitely until a `break` statement is executed.
- The first line in the loop uses the `recv` method of the socket object to receive up to 4096 bytes of data at a time from the whois server. The `recv` method takes an integer as an argument, which specifies the maximum number of bytes to          receive. The `recv` method returns a bytes object, which is assigned to the variable `data`.
- The next line checks if the `data` variable is empty, which means no more data is available from the server. If this is the case, the loop is terminated by a `break` statement.
   ## **Decoding the message object**
- The next line appends the received data to the `msg` object, which accumulates all the data from the server.
- The next line in the try block uses the `close` method of the socket object to close the connection to the whois server. This is a good practice to free up the resources used by the socket.
- The next line decodes the `msg` object to a string using utf-8 encoding, which is the standard encoding for whois information. The decoded string is assigned to the same variable `msg`.
   ## **Printing the whois information**
- The next line prints the `msg` string to the standard output, which is the console by default. The `msg` string contains the whois information of the domain name, such as the registrant, the registrar, the creation date, the expiration date,      the name servers, and other details.
- The first line in the except block prints the `socket.error` exception to the standard output, which contains the error message and the error code of the socket error.

   ## **Installation in Windows**
- A prerequisite for working with a domain is to install whois.

  https://learn.microsoft.com/en-us/sysinternals/downloads/whois
  
   ## **Installation on Linux**
  
- Update your .deb repos by running.

  ```console
  $ sudo apt update
  ```
- Apply any pending security or apps updates to your Linux box.

  ```console
  $ sudo apt upgrade
  ```

- Then install the whois client on Debian or Ubuntu Linux using the apt command or apt-get command.

  ```console
  $ sudo apt install whois
  ```
  ![Step-2](https://github.com/user-attachments/assets/aa58f6ff-1563-4c3a-b3bf-c49d00ac7c7e)


- Test it using the whois command for IP address lookup. For example.

```console
$ whois 142.250.192.78
$ whois 2404:6800:4007:817::200e
```
- Sample outputs.

```console
% [whois.apnic.net]
% Whois data copyright terms http://www.apnic.net/db/dbcopyright.html
 
% Information related to '2404:6800::/32'
 
% Abuse contact for '2404:6800::/32' is 'noc@google.com'
 
inet6num:       2404:6800::/32
netname:        GOOGLE_IPV6_AP-20080930
descr:          Google IPv6 address block in AP
country:        AU
org:            ORG-GIL3-AP
admin-c:        AC1668-AP
tech-c:         AC1668-AP
abuse-c:        AG738-AP
status:         ALLOCATED PORTABLE
mnt-by:         APNIC-HM
mnt-lower:      MAINT-GOOGLE-AP
mnt-routes:     MAINT-GOOGLE-AP
mnt-irt:        IRT-GOOGLE-AP
last-modified:  2020-05-26T18:20:48Z
source:         APNIC
....
..
....
source:         APNIC
 
person:         APNIC Contact
address:        1600 Amphitheatre Parkway, Mountain View, CA 94043
country:        US
phone:          +1-650-253-0000
e-mail:         apnic-contact@google.com
nic-hdl:        AC1668-AP
mnt-by:         MAINT-GOOGLE-AP
last-modified:  2020-05-26T18:05:41Z
source:         APNIC
 
% This query was served by the APNIC Whois Service version 1.88.15-SNAPSHOT (WHOIS-JP3)
```
- Then you can also do the domain name lookup. For instance.
```console
$ whois domain-name-here
$ whois cyberciti.biz
$ whois google.com
$ whois nixcraft.com
```
- Here is what you may see.

```console
Domain Name: GOOGLE.COM
   Registry Domain ID: 2138514_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.markmonitor.com
   Registrar URL: http://www.markmonitor.com
   Updated Date: 2019-09-09T15:39:04Z
   Creation Date: 1997-09-15T04:00:00Z
   Registry Expiry Date: 2028-09-14T04:00:00Z
   Registrar: MarkMonitor Inc.
   Registrar IANA ID: 292
   Registrar Abuse Contact Email: abusecomplaints@markmonitor.com
   Registrar Abuse Contact Phone: +1.2083895740
   Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
   Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited
   Domain Status: serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited
   Domain Status: serverTransferProhibited https://icann.org/epp#serverTransferProhibited
   Domain Status: serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited
   Name Server: NS1.GOOGLE.COM
   Name Server: NS2.GOOGLE.COM
   Name Server: NS3.GOOGLE.COM
   Name Server: NS4.GOOGLE.COM
   DNSSEC: unsigned
....
...
....
data, or email to MarkMonitor (or its systems) or the domain name contacts (or
its systems).
 
MarkMonitor reserves the right to modify these terms at any time.
 
By submitting this query, you agree to abide by this policy.
 
MarkMonitor Domain Management(TM)
Protecting companies and consumers in a digital world.
 
Visit MarkMonitor at https://www.markmonitor.com
Contact us at +1.8007459229
In Europe, at +44.02032062220
```
- Examples Here are my most common examples of the whois command under a Debian or Ubuntu Linux.
  
```console
$ Getting information about a domain name
$ whois <domain-name>
$ whois cyberciti.biz
```
- Finding information about an IP address

```console
$ whois <IPv4-here>
$ whois <IPv6-here>
$ whois 1.0.0.1
```
- Locating abuse contact for an IP address

```console
$ whois -b <IPv4-here>
$ whois -b <IPv6-here>
$ whois -b 8.8.4.4
```

   ## **Stay in touch with us💬**
