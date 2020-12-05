import socket

HEADER = 64
PORT = 5050
SERVER = "192.168.153.1"
# public ip : 27.7.109.26i
#print(SERVER)
FORMAT = 'utf-8'
ADDR = (SERVER,PORT)
DISCONNECT_MSG = "!!!DISCONNECT!!!"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    client.connect(ADDR)
except:
    print("[Connection Lost]......")
    exit()

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!!")
input()
send("Im Rishab")
input()
send("Ravi Kumar")
send(DISCONNECT_MSG)
