import pyttsx3
import speech_recognition as sr
import datetime
import os
import pywhatkit
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except:
            return "some error occurred, sorry from Jarvis"

def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        say("Good Morning!")
    elif 12 <= hour < 18:
        say("Good Afternoon!")
    else:
        say("Good Evening!")
    say("I am Jarvis. Tell me how can I help you!")

if __name__ == '__main__':
    say("Hello boss!")
    wish()

    sites = [
        ['youtube', 'https://www.youtube.com'],
        ['google', 'https://www.google.com'],
        ['facebook', 'https://www.facebook.com'],
        ['instagram', 'https://www.instagram.com'],
        ['my portal', 'http://tkrec.in/student/']
    ]

    while True:
        print("Listening...")
        query = takeCommand().lower()

        # Open Websites
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"opening {site[0]} sir....")
                webbrowser.open(site[1])

        # Responses
        if "hi jarvis" in query:
            say("Hi ramu sir.")
        elif "jarvis" in query:
            say("Hi Ramu sir.")
        elif "hello jarvis" in query:
            say("Hello Rachel madam.")
        elif "how are you" in query:
            say("I am fine. How are you?")
        elif "email password" in query:
            say("9908584745 sir.")
        elif "open music" in query:
            musicPath = r"C:\Users\pramu\Downloads\[iSongs.info] 01 - Chirunama Thana Chirunama.mp3"
            os.startfile(musicPath)
        elif "open photo" in query:
            photoPath = r"C:\Users\pramu\Downloads\keerthana.jpg"
            os.startfile(photoPath)
        elif "good night" in query:
            say("Good night madam.")
        else:
            say("Say it again.")
