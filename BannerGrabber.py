import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)  # Set a timeout for the connection
    print(s.recv(1024))

def main():
    ip = input("Enter the IP address to scan: ")
    port = int(input("Enter the port number to scan: "))
    banner(ip, port)

main()