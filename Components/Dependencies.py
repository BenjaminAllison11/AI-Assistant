from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import os
import requests

user = os.getlogin()
#speech recognition initialization
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)#0=male, 1=female
activationWord = 'computer' 


def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()



def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 1
        input_speech = listener.listen(source)

    try: 
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en_US')
        print(f'The input speech wasL {query}')
    except Exception as exception:
        print('I did not manage to catch that')
        speak('I did not manage to catch that')
        print(exception)
        return 'None'
    return query

query = parseCommand().lower().split()