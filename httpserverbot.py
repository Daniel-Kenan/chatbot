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
assistant.load_model(model)


