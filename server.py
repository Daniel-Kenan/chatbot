from _settings import *
from main import assistant
clients = []
nicknames = []
app = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
app.bind((settings["host"],settings["port"]))
app.listen(settings["que"]) 

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(settings["buffer_size"])
            message = str(assistant.request(message)).encode(settings["encoding"])
            broadcast(message)
        except:
            index = clients.index('client')
            clients.remove(client)
            client.close()
            nickname = nicknames["index"]
            nicknames.remove(nickname)
            print(f'{nickname} has left the chat'.encode(settings["encoding"]))
            break

def receive():
    while True:
        client, address = app.accept()
        print(f"Connected with {address}")
        client.send("NICK".encode(settings["encoding"]))
        nickname = client.recv(settings["buffer_size"]).decode(settings["encoding"])
        nicknames.append(nickname)
        clients.append(client)
        broadcast(f'{nickname} has joined the chat'.encode(settings["encoding"]))
        client.send("connected to the server".encode(settings["encoding"]))
        thread = threading.Thread(target = handle,args=(client,))
        thread.start()

print(f'|> Server is listening on {settings["host"]}:{settings["port"]}')
receive()