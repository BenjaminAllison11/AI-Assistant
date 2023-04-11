from Components.Dependencies import user, parseCommand, speak, activationWord, query, engine, voices, webbrowser, pyttsx3, os
from Components.Greeting import greeting
from Components.Websearch import websearch
from Components.Wikipedia import wikipedia
from Components.Log import log
from Components.Joke import joke
from Components.Gmail import gmail
from Components.Compliment import compliment
from Components.Dictionary import define
#Main loop

def main_loop(query):
    speak(f'Hello {user}, what may I do for you today?', 90)
    while True:
        query = parseCommand().lower().split()
        if query[0] == activationWord:
            query.pop(0)
            greeting(query)
            websearch(query)
            wikipedia(query)
            log(query)
            joke(query)
            gmail(query)
            compliment(query)
            define(query)          
        if query[0] == 'exit':
            speak('Goodbye')
            break


main_loop(query)