import asyncio
import websockets
from httpserverbot import assistant
# python -m websockets ws://localhost:8765
from time import time
import os

PORT = 8765
HOST = '0.0.0.0'

ALLOWED_HOSTS = [
   "https://strawberrysoft.co.za",
   "http://www.strawberrysoft.co.za",
   "https://www.strawberrysoft.co.za",
   "https://www.strawberrysoft.co.za/"
   "http://localhost:3000/",
   "http://localhost:3000",
   "localhost:3000",
   "http://localhost:5500/",
   "http://localhost:5500",
   "localhost:5500",
   "http://127.0.0.1:5500/",
   "http://127.0.0.1:5500",
   "127.0.0.1:5500"
   ]

agents = ["agent"]
chatrooms = {}

user = []
admin = []
async def handler(websocket, path):
  fingerprint = await websocket.recv()
  room = fingerprint
  if room not in chatrooms and fingerprint not in agents:
     chatrooms[room] = {} # create room
     chatrooms[room]["dialogue"] = []
     chatrooms[room]["time"] = time()
     chatrooms[room]["user"] = websocket  # put the user in the room

  elif fingerprint in agents:
     room = await websocket.recv() # get the room where the agent needs to go 
     print("agent room",room)
     try:
      chatrooms[room]["agent"] = websocket  # put the agent in the room 
     except: 
        chatrooms[room] = {}
        chatrooms[room]["dialogue"] = []
        chatrooms[room]["agent"] = websocket

  else:chatrooms[room]["user"] = websocket # else the user is returning in this room
  while True:
    conversation = chatrooms[room]["dialogue"]
    try:
        msg = await websocket.recv()
        
        if fingerprint in agents:
           try:
              await chatrooms[room]["user"].send(msg)
              chatrooms[room]["dialogue"] += [[fingerprint,msg]]
           except: await websocket.send("no user in this room")
        else: 
           try:
              await chatrooms[room]["agent"].send(msg)
              chatrooms[room]["dialogue"] += [[fingerprint,msg]] 
           except: 
              await websocket.send(assistant.request(msg))
                                   
    except websockets.ConnectionClosedOK : break
  

print(f"I am RUNNING ON PORT : {PORT}")
start_server = websockets.serve(handler, host = HOST, port = PORT,origins=ALLOWED_HOSTS)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
