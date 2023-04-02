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
joke_response = requests.get("https://v2.jokeapi.dev/joke/Any")
compliment_response = requests.get("https://complimentr.com/api")

#browser config, set path
opera_path = r"C:\Users\benja\AppData\Local\Programs\Opera GX\launcher.exe"
webbrowser.register('opera', None, webbrowser.BackgroundBrowser(opera_path))


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

def search_wikipedia(query = ''):
    searchresults = wikipedia.search(query)
    if not searchresults:
        print('no wikipedia result')
        return 'No result received'
    try:
        wikiPage = wikipedia.page(searchresults[0])
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    return wikiSummary


#Main loop

if __name__== '__main__':
    speak(f'Hello {user}, what may I do for you today?', 120)
    
    while True:


        #parse as a list
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            #list commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak(f'Hello {user}')
                else:
                    query.pop(0) #remove say
                    speech = ' '.join(query)
                    speak(speech)

            #searching
            if len(query) >= 2 and query[0] in ['go', 'look', 'search'] and query[1] in ['to', 'for', 'up']:
                if query[1] == 'to':
                    #use query to go to a site
                    speak('Opening browser...')
                    query = ' '.join(query[2:])
                    webbrowser.get('opera').open_new(query)
                else:
                    speak('Searching...')
                    query = ' '.join(query[2:])
                    webbrowser.get('opera').open_new('https://www.bing.com/search?q=' + query)

            #wikipedia
            if query[0] == 'wikipedia':
                query = ' '.join(query[1:])
                speak('Browsing Wikipedia for your information')
                speak(search_wikipedia(query))

            if query[0] == 'log':
                speak('Ready to record your notes')
                newNote = parseCommand().lower()
                now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                with open('note_%s.txt' % now, 'w') as newFile:
                    newFile.write(newNote)
                speak('Note written')

            if query[0] == 'tell' and query[1] == 'me' and query[2] == 'a' and query[3] == 'joke':
                if joke_response.status_code == 200:
                    joke = joke_response.json()
                    if joke['type'] == "single":
                        speak(joke["joke"])
                    if joke['type'] == "twopart":
                        speak(joke["setup"])
                        speak(joke["delivery"])
                else:
                    speak('Sorry, I could not get you a joke')
                           
            if query[0] == 'i' and query[1] == 'need' and query[2] == 'to' and query[3] == 'send' and query[4] == 'an' and query[5] == 'email':
                speak('Bringing up g-mail now')
                webbrowser.get('opera').open_new('https://mail.google.com/mail/u/0/#inbox?compose=new')
                       
            if query[0] == 'Compliment' or query[0] == 'complement' and query[1] == 'me':
                if compliment_response.status_code == 200:
                    compliment = compliment_response.json()
                    speak(compliment["compliment"])

            
            if query[0] == 'exit':
                speak('Goodbye')
                break