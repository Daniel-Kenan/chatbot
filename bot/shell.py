import sys,os
import tensorflow as tf
from bot import GenericAssistant
_current_dir = os.path.dirname(os.path.realpath(__file__))
assistant = GenericAssistant( model_name="Luffy")
model = os.path.join(_current_dir,"models",assistant.model_name)


# def func():
#     print('intetion ruuning')

# mappings = {'greetings',func}
try: 
    try:
      if (sys.argv[1]) == "--shell" : None
    except: 
        raise BaseException('')
    assistant.load_model(model)
    done = False
    while not done:
       message = input("Enter a message: ")
       
       if message == "STOP":
           done = True
       else:
           response = assistant.request(message)
           print(response)
           print(assistant)
except KeyboardInterrupt: exit()
except:
    print("training the model")
    assistant.train_model()     
    assistant.save_model(model)
