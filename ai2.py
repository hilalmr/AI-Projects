#MODULES
import pyttsx3 
import speech_recognition as sr
from datetime import datetime
import subprocess
import os
import ctypes
import pyautogui
from rich.console import Console                                                      
from rich.table import Table
from time import sleep
from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
import itertools
import gtts
import time
import playsound





engine = pyttsx3.init() 
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

r = sr.Recognizer()




num = 10
for _ in itertools.repeat(None, num):
    r = sr.Recognizer()



with sr.Microphone() as source:
    print("Speak Anything...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))

        #!Commands for the ai to speak

        #?Hello        
        if text=='hello':

            engine.say('Hi there!')
            engine.runAndWait()

        #?Name 

        if text=='what is your name':

            engine.say('My name is Terra ')
            engine.runAndWait()

        #?Time

        if text=='time':

            engine.say(current_time)
            engine.runAndWait()
        if text=='what is the time':

            engine.say(current_time)
            engine.runAndWait()


        #! Date

        if text=='what is the date':
                
                engine.say(now.strftime("%Y-%m-%d"))
                engine.runAndWait()

        if text=='what is todays date':
                
                engine.say(now.strftime("%Y-%m-%d"))
                engine.runAndWait()

        if text=='date':
                
                engine.say(now.strftime("%Y-%m-%d"))
                engine.runAndWait()

            
        #*Open notepad

        #

        if text=='open note':

            engine.say('Opening Notepad')
            engine.runAndWait()

            subprocess.Popen("C:\\Windows\\System32\\notepad.exe")

        #!Lock screen

        if text=='lock screen':

            ctypes.windll.user32.LockWorkStation()
        if text=='lock':
            ctypes.windll.user32.LockWorkStation()

        #!Close app

        if text=='close the app':

            pyautogui.hotkey('alt','f4')

        #*Open paint

        if text=='open paint':

            engine.say('Opening Paint')
        if text=='open Paint':

            engine.say('Opening Paint')
            engine.runAndWait()
            subprocess.Popen("C:\WINDOWS\system32\mspaint.exe")

        #?Calculator

        if text=='calculator':
            
            engine.say('Type you first number to be added')
            engine.runAndWait()

            num1 = input("Number1: ")
            engine.say('Type you second number to be added')
            engine.runAndWait()

            
            num2 = input("Number2: ")

            sum = int(num1) + int(num2)

            print(int(num1) + int(num2))

            engine.say(sum)
            engine.runAndWait

        #^To show commands
        if text=='commands':

            
            table = Table(title="help")

            table.add_column("Sl.no", style="yellow", no_wrap=True)
            table.add_column("Command", style="red")

            table.add_row("1", "lock", )
            table.add_row("2", "hello",)
            table.add_row("3", "what is the time",)
            table.add_row("4", "what is your name", )
            table.add_row("5", "open note",)
            table.add_row("6", "open paint",)
            table.add_row("7", "application",)
            table.add_row("8", "calculator",)


            console = Console()
            console.print(table, justify="center")

        if text=='bruh':
            engine.say('BRUHHHHHHH')
            engine.runAndWait()
            engine.say('BRUHHHHHHH')
            engine.runAndWait()
            engine.say('BRUHHHHHHH')
            engine.runAndWait()
            print("BRUHHHHHHH")

        if text=='game':
            subprocess.Popen(['D:\\Minecraft\\.minecraft\\TLauncher.exe'])

        #* How are you
        if text=='how are you':
            engine.say('I am fine')
            engine.runAndWait()

        #! Shut up
        if text=='shut up':
            print("ok")
            engine.runAndWait()

        


    except:
        print('Sorry can you repeat?')

        

  