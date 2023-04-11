from Components.Dependencies import requests, query, speak

compliment_response = requests.get("https://complimentr.com/api")

def compliment(query):
    if query[0] == 'Compliment' or query[0] == 'complement' and query[1] == 'me':
                if compliment_response.status_code == 200:
                    compliment = compliment_response.json()
                    speak(compliment["compliment"])