#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = '0.0.0.0' # Get local machine name
port = 12345                # Reserve a port for your service.


print('Server started!')
print('Waiting for clients...')

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

for i in range(5):
    c, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    msg = c.recv(1024)
    print(addr, ' >> ', msg , i)
    c.send(': Message sent by kaiser '.encode())

c.close()                # Close the connection