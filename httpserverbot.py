import tensorflow as tf
import sys,os
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
from socket import gethostname,gethostbyname

_current_dir = os.path.dirname(os.path.realpath(__file__))
_dir = os.path.join(_current_dir,"bot")
sys.path.insert(1, _dir)
from bot import GenericAssistant
assistant = GenericAssistant( model_name="Luffy")
model = os.path.join(_dir,"models",assistant.model_name)
global graph
graph = tf.get_default_graph()
assistant.load_model(model)
host = gethostbyname(gethostname())
serverPort = 5000
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "json")
        self.end_headers()
        json_ = {'text':assistant.request(self.path[1:])}
        self.wfile.write(bytes(json.dumps(json_),"utf-8"))
   
if __name__ == "__main__":        
    webServer = HTTPServer((host, serverPort), MyServer)
    print("Server started http://%s:%s" % (host, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
