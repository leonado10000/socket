import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
host = "192.168.0.187"
port = 300

s.bind((host,port))
s.listen()
print("Waiting for player 1")
p1,adr1 = s.accept()
print("Waiting for player 2")
p2,adr2 = s.accept()
