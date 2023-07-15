import socket

HEADER = 64
CLIENT_NUMBER = "10"
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "172.20.208.1"

PORT = int(input("Please enter integer between 1 and 100: "))
ADDR = (SERVER, PORT)
NAME_CLIENT = "Client of John Q. Smith"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

#client name
send(f"{NAME_CLIENT}")
#client number
send(str(CLIENT_NUMBER))
#server number
send(str(PORT))

server_name = client.recv(HEADER).decode(FORMAT)
print(f'[server name] {server_name}')
server_port = client.recv(HEADER).decode(FORMAT)
print(f'[server port] {server_port}')
send(DISCONNECT_MESSAGE)