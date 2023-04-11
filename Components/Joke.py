from Components.Dependencies import query, requests, speak 
joke_response = requests.get("https://v2.jokeapi.dev/joke/Any")

def joke(query):
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