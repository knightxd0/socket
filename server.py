import socket
import threading

HEADER = 64
PORT = 50
SERVER = "172.20.208.1" #socket.gethostbyname(socket.gethostname()) ใช้ IP ในเครื่อง
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECTION_MESSAGE = "!DISCONNECT"
NAME_SERVER = "Server of John Q. Smith"


server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    sum = 0
    
    # conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    i = 0
    while connected:
        conn.send(NAME_SERVER.encode(FORMAT))
        conn.send(str(PORT).encode(FORMAT))
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
        
            if msg == DISCONNECTION_MESSAGE:
                connected = False
            
            if i == 0:
                print(f"Client name: {msg}")
                i = i+1
            elif i == 1:
                print(f"client number: {msg}")
                sum = sum + int(msg)
                i = i+1
            elif i == 2:
                print(f"server number: {msg}")
                i = i+1
                sum = sum + int(msg)
                print(f"sum value: {sum}")
            elif i == 3:
                print(f"[{addr}] {msg}")
                i = 0
            
            
                
            
            
    conn.close()
         

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()

