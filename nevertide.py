import ctypes
import os
import signal
import sys
import time
import uuid
import discord
import pygame
import random
from dotenv import load_dotenv
from elevenlabs import ElevenLabs
from win10toast import ToastNotifier
import customtkinter as ctk

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def run_as_admin():
    """
    If not admin, relaunch the current script as admin and exit this process.
    Call this once from your main script.
    """
    if is_admin():
        return

    params = " ".join(sys.argv[1:])
    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        sys.executable,
        f'"{sys.argv[0]}" {params}',
        None,
        1,
    )
    



def speak_tts(text, apikey):
    client = ElevenLabs(api_key=apikey)
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    filename = f"tts_{uuid.uuid4().hex}.mp3"

    audio = client.text_to_speech.convert(
        voice_id="bIHbv24MWmeRgasZH58o",
        text=text,
        model_id="eleven_multilingual_v2",
    )

    with open(filename, "wb") as f:
        for chunk in audio:
            f.write(chunk)

    sound = pygame.mixer.Sound(filename)
    sound.play()

    while pygame.mixer.get_busy():
        time.sleep(0.1)

    os.remove(filename)


def tempfullimage(path,timey):
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Splash")

    image = pygame.image.load(path)
    w, h = screen.get_size()
    image = pygame.transform.scale(image, (w, h))
    screen.blit(image, (0, 0))
    pygame.display.update()
    pygame.event.pump()

    hwnd = pygame.display.get_wm_info()["window"]

    SW_SHOW = 5
    HWND_TOPMOST = -1

    ctypes.windll.user32.ShowWindow(hwnd, SW_SHOW)
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    ctypes.windll.user32.SetWindowPos(
        hwnd,
        HWND_TOPMOST,
        0,
        0,
        0,
        0,
        0x0001 | 0x0002,
    )

    time.sleep(timey)
    pygame.quit()


def sendnotification(title, message, icon, time_):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, icon_path=icon, duration=time_, threaded=True)


def playsound(path):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound(path)
    sound.play()


def reload():
    script_path = os.path.abspath(sys.argv[0])
    os.startfile(script_path)
    os.kill(os.getpid(), signal.SIGTERM)


def quit():
    os.kill(os.getpid(), signal.SIGTERM)



class CreateDiscord():
    """MGHH - Discord Variable
    -
    This class creates a discord bot for you to use!"""
    def __init__(self):
        """This is where you would make the bot function the heart"""
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self.client = discord.Client(intents=self.intents)
        self.TasksOnStart_M=[]
        self.ResponseMessagesReply={}
        self.ResponseMessages={}
        self.CommandsMessages={}
        self.InMessages={}
        self.RunOnStart=[]
        self.AnyMessageResponsCommand=""
        @self.client.event
        async def on_ready():
            for Task in self.TasksOnStart_M:
                await self.message(Task[0],Task[1])
            for Task in self.RunOnStart:
                await Task()

            print(f"Ready on {self.client.user}")
        @self.client.event
        async def on_message(message):
            if(message.content.lower() in self.ResponseMessagesReply) and (message.author != self.client.user):
                Reply=self.ResponseMessagesReply[message.content.lower()]
                await message.channel.send(Reply,reference=message)
            elif(message.content.lower() in self.ResponseMessages) and (message.author != self.client.user):
                Reply=self.ResponseMessages[message.content.lower()]
                await message.channel.send(Reply)
            elif(message.content.lower() in self.CommandsMessages) and (message.author != self.client.user):
                Command=self.CommandsMessages[message.content.lower()]
                await Command(message)
            for word in str(message.content).lower().split(" "):
                if (word in self.InMessages):
                    Reply=self.InMessages[word]
                    await message.channel.send(Reply)
            try:
                await self.AnyMessageResponsCommand(message)
            except:
                pass






    async def message(self,message,channel_id:int):
        channel = self.client.get_channel(channel_id)
        if(channel):

            await channel.send(message)
        else:
            print("ERROR")

    def RunBot_as_PlainToken(self,Token:str):
        """Runs Bot Without a Enverment Variable
        -----------
        str -> Token
        _______________

        """
        self.client.run(Token)

    def RunBot_as_EnvToken(self,TokenEnv:str):
        """Runs Bot With a Enverment Variable
        -----------
        str -> TokenEnv
        _______________
        This will be the Enverment Variable Name
        """
        Token=os.getenv(TokenEnv)

        self.client.run(Token)


    def schedulemessages(self, list):
        """
        Schedule a Start Message
        _
        list: this Requres ["string",Channel ID]
        """
        self.TasksOnStart_M.append(list)

    def AddResponseReplyMessages(self,message,response):
        """
        Respons After Message sent (Mentions)
        _
        This will discribe the [message] varibal and if that matches with the
        [Discord message]. Then it will respond with [response]

        (Can only happen one par line)

        """
        self.ResponseMessagesReply.update({message.lower():response})

    def AddResponse(self,message,response):
        """
        Respons After Message sent
        _
        This will discribe the [message] varibal and if that matches with the
        [Discord message]. Then it will respond with [response]

        (Can only happen one par line)

        """
        self.ResponseMessages.update({message.lower():response})

    def DoActionIf(self,message,command):
        """
        Respons a function after message==discord_message
        _
        Runs async functions

        """
        self.CommandsMessages.update({message.lower():command})

    def InMessageResponse(self,word,reply):
        """Replys to a message if it have a word in it"""
        self.InMessages.update({word.lower():reply})
    def AppenedRunCommand(self,command):
        """
        Runs async functions
        _

        """
        self.RunOnStart.append(command)

class gui():
    def __init__(self):
        self.guicompents={"Buttons":[]}
        self.root = ctk.CTk()
    def creategui(self, resolution):
        self.root.geometry(resolution)
    def settitle(self, title):
        self.root.title(title)
    def run(self):
        self.root.mainloop()
    def stopgui(self):
        self.root.destroy()
    def PlaceGUI(self,GUI:["button"],pos:tuple[(0,0)]):
        GUIID=random.randint(1,99999999)
        if GUI =="button":
            New=ctk.CTkButton(master=self.root)
            self.guicompents["Buttons"].append({"ID":GUIID,"Type":"button","Settings":New})
            New.place(x=pos[0],y=pos[1])
        print(self.guicompents)


