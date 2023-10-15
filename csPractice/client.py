import socket

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 56789

cli.connect((host,port))
print("Connected")
for i in range(5):
    msg  = input("Enter a message for server")
    cli.send(msg.encode())
    msg = cli.recv(1024)
    print(host+" :",msg)

cli.close()