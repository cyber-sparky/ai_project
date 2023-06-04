import speech_recognition as sr #pip install SpeechRecognition
import pyttsx3 # pip install pyttsx3
import datetime
import webbrowser # pip install webbrowser
import time
from pydub import AudioSegment # pip install pydub
from pydub.playback import play


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
r = sr.Recognizer()


def speak(*text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("good evening")
        print("Good Evening")

def takeCommand():
    global statement
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        print(statement)
        return statement
    

speak("Hello, Im Jexi")
wishMe()
arr = ["saran","balaji","mathan","prasanna","shashi","bharath","barath","rukmani","madhu bala","steffy","vishali","yogi","prathiusha","nithishri","arvind","aakash","denny","joel","sandeep","saraswathi","naresh","gokul","isaac","karthik","dharun","hemanath","jaleela","kingston","meganathan","nithilan","parameshwari","sri"]

if __name__ == "__main__":
    while True:
        speak("tell me how can i help you now")
        # statement = takeCommand().lower()
        if statement ==0:
            continue

        if "stop" in statement or "ok bye" in statement or "good bye" in statement:
            speak("Okay Good bye for now")
            break

        if "open google" in statement:
            speak("Opening google")
            webbrowser.open_new_tab("https://www.google.com/")
            time.sleep(5)

        if "open spotify" in statement:
            speak("Opening spotify")
            webbrowser.open_new_tab("https://open.spotify.com/")
            time.sleep(5)

        for i in range(len(arr)):
            if arr[i] in statement:
                song = AudioSegment.from_wav("./mp3/vituru.wav")
                print('playing sound using  pydub')
                play(song)
                time.sleep(5)

