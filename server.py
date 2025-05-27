import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()  # Get local machine name
port = 444  # Reserve a port for your service.

serversocket.bind((host, port))  # Bind to the port
serversocket.listen(3)  # Now wait for tcp client connection. 5 is the number of unaccepted connections that the system will allow before refusing new connections.

while True:
    clientsocket, address = serversocket.accept()  # Establish connection with client.
    print(f"Got a connection from {address}")
    message = "Thank you for connecting" + "\r\n"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()  # Close the connection