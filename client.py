import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()  # Get local machine name/IP address
port = 444

clientsocket.connect((host, port))  # Connect to the server

message = clientsocket.recv(1024)  # Receive data from the server, 1024 is the buffer size/maximum amount of data to be received at once
print(f"Received message: {message.decode('ascii')}")  # Decode the received bytes to string
clientsocket.close()  # Close the connection
