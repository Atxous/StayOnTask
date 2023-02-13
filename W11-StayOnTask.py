import webbrowser as web
import schedule, os
from ctypes import windll
from time import sleep
from playsound import playsound

def close():
    os.system("shutdown -t 0 -r -f")
    return schedule.CancelJob

def action():
    playsound("C:") #put the directory to your audio
    schedule.every(5).minutes.do(close)
    windll.user32.MessageBoxW(0, "\n\n      5 minutes remaining.      \n\n\n", "Calculus Time.", 0) 
     
schedule.every().day.at("19:00").do(action)

while True:
    schedule.run_pending()
    sleep(60)
