from Components.Dependencies import user, speak
def greeting(query):
    if len(query) > 1 and query[0] == 'say':
        if 'hello' in query:
            speak(f'Hello {user}')
        else:
            query.pop(0) 
            speech = ' '.join(query)
            speak(speech)