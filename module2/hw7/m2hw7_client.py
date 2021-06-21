from threading import Thread
import socket

HOST = '127.0.0.1'
PORT = 55555

s = socket.socket()
s.connect((HOST, PORT))

def listen():
    while True:
        message = s.recv(1024).decode()
        print(message)
        
t = Thread(target = listen)
t.daemon = True
t.start()

while True:
    message = input()
    
    if message == 'quit':
        break
    
    s.send(message.encode())

s.close()