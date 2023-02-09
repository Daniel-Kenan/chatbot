import sys,os
_current_dir = os.path.dirname(os.path.realpath(__file__))
_dir = os.path.join(_current_dir,"bot")
sys.path.insert(1, _dir)
from bot import GenericAssistant
import tensorflow as tf
assistant = GenericAssistant( model_name="Luffy")
model = os.path.join(_dir,"models",assistant.model_name)
global graph
graph = tf.get_default_graph()
# sess = tf.Session(graph=graph,config=session_conf)
assistant.load_model(model)

# assistant.train_model()     
# assistant.save_model(model)
# done = False
# while not done:
#     message = input("Enter a message: ")
#     if message == "STOP":
#         done = True
#     else:
#         response = assistant.request(message)
#         print(type(response))

# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 5000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "json")
        self.end_headers()
        self.wfile.write(bytes(f"{'{text:'+assistant.request(self.path[1:])+'}'}", "utf-8"))
   

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
