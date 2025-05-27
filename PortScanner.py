import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)  # Set a timeout for the connection

host = input("Please enter the IP you want to scan: ")  # Get the local machine name
port = int(input("Please enter the port you want to scan: ")) # 21 - ftp, 22 - ssh, 23 - telnet, 25 - smtp, 53 - dns, 80 - http, 110 - pop3, 143 - imap, 443 - https

def portScanner(port):
    if s.connect_ex((host, port)):
        print(f"Port {port} is closed")
    else:
        print(f"Port {port} is open")

portScanner(port) 
