import socket

s = socket.socket()
host = socket.gethostname()
port = 56789


# host = '0.0.0.0'
s.bind((host,port))
s.listen(5)
print("Server Started")
print("Server waiting for client\n")
clie, adrr = s.accept()
print("Client :",clie,"\nadress :",adrr, end="\n\n")
for i in range(5):
    msg = clie.recv(1024)
    print(clie.getsockname,":"+msg.decode())
    clie.send(input("Enter for client").encode())

s.close()