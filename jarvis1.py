import os
from pyexpat.errors import messages
import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pyjokes
from keyboard import press_and_release
import time
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices [0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


    
def wishme():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >=0 and hour <12:
        print(f"Good Morning , its {tt}")
        speak(f"Good Morning , its {tt}")

    elif hour >=12 and hour <18:
        print(f"Good Afternoon , its {tt}")
        speak(f"Good Afternoon, its {tt}")

    else:
        speak("good evening sir")

    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")

                
    
def takeCommand():

     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("listening...")
         r.pause_threshold = 1
         audio = r.listen(source)

     try:
         print("Recognizing")
         query = r.recognize_google(audio, language='en-in')
         print(f"User Said: {query}\n")

     except:
        #print(e)


        print("Say That again please...")
        return "none"
     return query


if __name__ == '__main__':
      wishme()
      while True:
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia",  "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open classroom' in query:
             webbrowser.open("https://classroom.google.com/u/1/h")

        elif 'open whatsapp' in query:
            webbrowser.open ("https://web.whatsapp.com/")

        elif 'play music' in query:
              Music_dir = 'C:\\Users\Lenovo\\OneDrive\\Desktop\\Music'
              songs = os.listdir(Music_dir)
              print(songs)
              os.startfile(os.path.join(Music_dir, songs[0]))

        elif 'open chrome' in query:
            codePath = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\Google Chrome.lnk"
            os.startfile(codePath)

        
        elif 'open spotify' in query:
            codePath = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\Spotify.lnk"
            os.startfile(codePath)
        
        elif 'open github' in query:
            webbrowser.open("https://github.com/")

        elif 'maths class' in query:
            webbrowser.open("https://us04web.zoom.us/j/7498167723?pwd=QVp2Ylh5VnFjY1I1UDNWaGxIeTZjUT09#success") 

        elif 'open discord' in query:
            codePath = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\Discord.lnk"  
            os.startfile(codePath)
             
        elif 'open epic' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Epic Games Launcher.lnk"
            os.startfile(codePath) 

        elif 'open word' in query:
            codePath  = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(codePath)

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")

        elif 'play light switch' in query:
            webbrowser.open("https://open.spotify.com/track/1BSMpVGWs3v5BZKnAQziAc?si=a0d08560e784438d")   

        elif 'play the best' in query:
            webbrowser.open("https://open.spotify.com/playlist/6bpurZ7Cf6TWfczzSadBYk?si=1b39aebb682142da") 
        
        elif 'play baraat' in query:
            webbrowser.open("https://open.spotify.com/track/0YLSjVxSb5FT1Bo8Tnxr8j?si=8e6854752c894393")

        elif 'launch fortnite' in query:
            codePath = "C:\\Users\\Lenovo\\OneDrive\Desktop\\Fortnite.url"
            os.startfile(codePath)

        elif 'open vmware' in query:
            codePath = "C:\\Users\\Lenovo\\OneDrive\\Desktop\\VMware Workstation 16 Player.lnk"
            os.startfile(codePath)

        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Roaming\Microsoft\\Windows\\start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'bye' in query:
            speak("OK sir bye Talk to you soon , just say Jarvis")
            break           
        
        elif 'hello how are you' in query:
            speak("Hello , i am fine")

        elif "search" in query and "youtube" in query:
            query = query.replace("search", "")
            query = query.replace("on youtube", "")
            query = query.replace("youtube", "")
            string = query.split()
            search = ""
            for i in string:
                search += i

                search += "+"
            webbrowser.open(f"https://www.youtube.com/results?search_query={search}")

        if 'pause' in query:
            press_and_release('space bar')

        elif 'play' in query:
            press_and_release('k')

        elif 'full screen' in query:
            press_and_release('f')

        elif 'normal mode' in query:
            press_and_release('f')

        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')

    
        elif 'who are the best grandparents in the world' in query:
            speak("ofc it is nani vyas and nanu vyas")

        elif 'who are you' in query:
              h_dir = 'C:\\Users\\Lenovo\\OneDrive\\Desktop\\h'
              songs = os.listdir(h_dir)
              os.startfile(os.path.join(h_dir, songs[0]))

        elif 'good one' in query:
            speak("thank you sir")

        elif 'who is your favourite actor' in query:
            speak("Tom Cruise is my favourite actor")

        elif 'good morning' in query:
            speak("good morning sir")

        elif 'restart' in query:
            os.system('shutdown /r /t 1')

        elif 'new tab' in query:
            press_and_release('ctrl+t')  
            
        elif "what do you think of my elder sister" in query:
            speak("stupid Girl")

        elif  'destroy the world' in query:
          speak("initiating , airstrike , sequence in ten , nine , eight , seven , six  , five , four , three , two , one , airstrike sequence succesfull")


        elif "search" in query and "google" in query:
            query = query.replace("search", "")
            query = query.replace("on google", "")
            query = query.replace("google", "")
            string = query.split()
            search = ""
            for i in string:
                search += i


            webbrowser.open(f"https://www.google.com/search?q={search}&rlz=1C1VDKB_enIN990IN990&oq=photo&aqs=chrome..69i57j35i39j0i67i433j0i67j0i67i433j0i131i433i512j0i67i433j0i67i131i433j0i67i433j0i433i512.1117j0j15&sourceid=chrome&ie=UTF-8")

        elif 'continue' in query:
            import pyautogui as spam
            
            limit = input("number of messages")
            msg = input("enter the message")



            i = 0

            time.sleep(5)

            while i<int(limit):

             spam.typewrite(msg)
            spam.press('Enter')
            i+=1