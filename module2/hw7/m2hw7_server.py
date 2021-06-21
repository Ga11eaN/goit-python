import socket
from threading import Thread

HOST = '127.0.0.1'
PORT = 55555

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(100)

list_of_clients = []

def clientthread(conn,addr):
    
    conn.send('Welcome to chat!'.encode())
    
    while True:
        try:
            message = conn.recv(1024).decode()
            print('['+ addr[0] + ':' + str(addr[1]) + ']' + message)

        except Exception as e:
            print(f"[!] Error: {e}")
            list_of_clients.remove(conn)
        
        for sock in list_of_clients:
            sock.send(('['+ addr[0] + ':' + str(addr[1]) + ']' + message).encode())
        

while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + ':' + str(addr[1]) + ' connected!')
    t = Thread(target = clientthread, args = (conn,addr,))
    t.daemon = True
    t.start()


for cs in list_of_clients:
    cs.close()

s.close()
