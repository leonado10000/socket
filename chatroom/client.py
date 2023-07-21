import threading
import socket
alias = input("Enter an alias :")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))

def client_receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == "alias?" :
                client.send(alias.encode('utf-8'))
            else:
                print(msg)
        except:
            print("Error !!!")
            client.close()
            break


def client_send():
    while True:
        msg = f'{alias}: {input("")}'
        client.send(msg.encode('utf-8'))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()