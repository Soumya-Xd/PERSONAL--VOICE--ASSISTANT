import pyttsx3
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit
import wikipedia
from googletrans import Translator
import os
import pyautogui
import psutil
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests
from tkinter import Tk
from gtts import gTTS
from tkinter import StringVar
import PyPDF2
from pytube import YouTube
import datetime
from playsound import playsound
import keyboard
import pyjokes
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',200)

def Speak(Audio):
    print("   ")
    print(f": {Audio}")
    engine.say(Audio)
    print("    ")
    engine.runAndWait()

def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("AI...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    return query.lower()

def TaskExe():

    def Music():
        Speak("Tell Me The NamE oF The Song!")
        musicName = takecommand()
        
        if 'akeli' in musicName:
            os.startfile('E:\\Songs\\akeli.mp3')
        elif 'blanko' in musicName:
            os.startfile('E:\\Songs\\blanko.mp3')    
        else: 
            pywhatkit.playonyt(musicName)

        Speak("Your Song Has Been Started! , Enjoy!")

    def OpenApps():
        Speak("Ok  , Wait A Second!")
        
        if 'open code' in query:
            os.startfile("E:\\Applications\\Microsoft VS Code\\Microsoft VS Code\\Code.exe")

        
        elif 'open chrome' in query:
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        
        elif 'open facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif ' open instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif ' open maps' in query:
            webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com')

        Speak("Your Command Has Been Completed!")

    def Temp():
        search = "temperature in delhi"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The Temperature Outside Is {temperature} ")

        Speak("Do I Have To Tell You Another Place Temperature ?")
        next = takecommand()

        if 'yes'or'yeah' in next:
            Speak("Tell Me The Name Of tHE Place ")
            name = takecommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Speak(f"The Temperature in {name} is {temperature}")

        else:
            Speak("no problem")

    

    def CloseAPPS():
        Speak("Ok  , Wait A second!")

        if 'open youtube' in query:
            os.system("C:\Program Files\Google\Chrome\Application")

        elif 'open chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        
        elif 'open code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'open instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        Speak("Your Command Has Been Succesfully Completed!")

    def YoutubeAuto():
        Speak("Whats Your Command ?")
        comm = takecommand()

        if 'stop' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        Speak("Done")

    
        
    def ChromeAuto():
        Speak("Chrome Automation started!")

        command = takecommand()

        if 'close the tab' in command or 'close tab'in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')
            
        elif 'reopen closed tab' in command:
            keyboard.press_and_release('ctrl +shift+ t') 
        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl +h')
        elif 'check download' in command:
            keyboard.press_and_release('ctrl +j')
    def screenshot():
        Speak("Ok Boss , What Should I Name That File ?")
        path = takecommand()
        path1name = path + ".png"
        path1 = "F:\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("F:\\")
        Speak("Here Is Your ScreenShot") 
    def Date():
        date=datetime.datetime.now().strftime("%B,%d,%Y")
        Speak(f"The current date is {date}")
        print("===>",date)
    while True:

        query = takecommand()

        if 'hello' in query or 'hello jervis'in query or'jervis'in query or'hey'in query or 'hi jervis'in query or'hello whats your name? 'in query:
            Speak("Hello sir , I Am JARVIS .")
            Speak("Your Personal AI Assistant!")
           
        elif 'the time' in query or 'whats the time 'in query or 'can you plaese tell me the time?'in query or 'jervis tell me the time?'in query or 'show me the time' in query:
            
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {strTime}")            
            
        elif 'the date'in query or 'Whats the date?'in query or 'can you show me the the date' in query or 'jervis tellme the date?'in query:
            Date()

        elif 'how are you' in query or 'jarvis how you'in query :
            Speak("I Am Fine!")
            Speak("Whats About YOU?")
        elif 'happy?'in query:
            Speak('Yes sir I am very happy thank you sir for asking me that ')
        elif ' created'in query:
            Speak('actually i have been created by soumya singha roy.')    
        elif 'fine' in query:
            Speak("OK Good")
            Speak("How May I Help You?")
        elif 'Thank you' in query or 'thanks'in query:
            Speak("Welcome")
        elif 'ok now tell me' in query :
            Speak("What should i tell please ask me?")
        

        elif ' i think you need a break' in query or'take a break'in query:
            Speak("Ok Sir , You Can Call Me Anytime !")
            Speak("Just Say Wake Up Jarvis and press the ctrl+alt+n button.!")
            break
        elif 'bye'in query or 'buy'in query:
            Speak("Bye")
            Speak("See you later")
            break
        elif 'youtube search' in query:
            Speak("OK  , This Is What I found For Your Search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done! is anything you want to search?")

        elif 'website' in query:
            Speak("Ok Sir , Launching.....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'launch' in query or 'open website'in query:
            Speak("Tell Me The Name Of The Website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("allright Sir!")

        elif 'wikipedia' in query or 'make a wikipedia search'in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif 'screenshot' in query:
            screenshot()

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()
            
        elif 'open telegram' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'close chrome' in query:
            CloseAPPS()

        elif 'music' in query:
            Music()

        elif 'close telegram' in query:
            CloseAPPS()

        elif 'close instagram' in query:
            CloseAPPS()

        elif 'close facebook' in query:
            CloseAPPS()

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'reload' in query:
            keyboard.press_and_release('ctrl + alt + n')   

        elif 'close the tab' in query or 'jervis closed the tab'in query or 'close tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query or 'jervis open new tab' in query or 'open a tab'in query or 'new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl +h')

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'joke' in query or 'tell me joke'in query or 'tell some joke'in query or 'tell me another joke'in query or 'one more jokes please'in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'tell my word' in query or 'say what i am told'in query or'you will tell my word'in query or 'jaris repeat my word'in query or 'jarvis tell what i am saying?'in query:
            Speak(" ok Speak i will try my best!")
            jj = takecommand()
            Speak(f"{jj}")

        elif 'my location' in query or 'can you tell my location'in query or ' show my location'in query or 'search my location'in query:
            Speak("Ok , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/@23.1071276,87.9530849,12z')

        elif 'alarm' in query or 'set an alarm'in query :
            Speak(" Please tell me The Time !")
            time = input("ENTER THE TIME:")
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time To Wake Up !")
                    playsound('C:\\Users\\Soumya\\Music\\So-Good.mp3')
                    Speak("Alarm Closed!")

                elif now>time:
                    break
        

        elif 'video downloader' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube Video Downloader")
            Speak("Enter Video Url Here !")
            Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
            link = StringVar()
            Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
            Entry(root,width = 70,textvariable = link).place(x=32,y=90)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

            Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

            root.mainloop()
            Speak("Video Downloaded")
            
      
        
        elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jarvis","")
            Speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            Speak("You Tell Me That" + remeber.read())

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("No Speakable Data Available!")

        elif 'how to' in query:
            Speak("Getting Data From The Internet !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)

        elif 'send message' in query:
            pywhatkit.sendwhatmsg('+918981113501','hlw ',18,15)
           # Speak ("Whom did I send the message please tell me the number")
            #sendmessage=input("Enter the Number:")
           # Speak ("Tell Me the messages!")
            #messages=input("Enter the Message:")
           # Speak("Tell Me The Time!")
           # time_min=input("Enter The Time")
            #while True:
              # if  sendmessage==time:
               #     Speak("MESSAGE SENT SUCCESFULLY")
             # #   #  Speak("Sorry Please check the number")
                 #   break


            
        elif 'temperature' in query:
            Temp()

     
TaskExe()