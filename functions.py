import tts
import wiki
#import screen_clear
import current_time
import v2t
import sqlite3, start
import os

def run(do):

    if 'wikipedia' in do.lower():
        output = wiki.search(do)
        return output    

    if 'current time' in do.lower():
        time = current_time.current_time()
        output = "The current time is "+time
        return output
        
    if 'face mask detect' in do.lower():
        import face
        face.mask_detection()
        
    if 'set alarm' in do.lower():
        os.system('alarmn.py 1')
        return "Alarm opened"

    if 'open contacts' in do.lower():
        os.system('contact.py 1')
        return "Contacts Opened"

    if 'do list' in do.lower():
        os.system('todo.py 1')
        return "Todo list opened"

    if 'sleep' in do.lower():
        return "sleep"    
            
