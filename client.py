from _settings import *

client  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((settings["host"],settings["port"]))

nickname = input("Choose a nickname: ")

def receive():
    while True:
        try:
            message = client.recv(settings["buffer_size"]).decode(settings["encoding"])
            if message == "NICK":
                client.send(nickname.encode(settings["encoding"]))
            else:
                print(message)
        except Exception as e:
            print(e)
            client.close()
            break

def send():
    while True:
        message = f'{nickname}: {input()}'
        client.send(message.encode(settings["encoding"]))
    

receive_thread = threading.Thread(target=receive)
receive_thread.start()
send_thread = threading.Thread(target=send)
send_thread.start()