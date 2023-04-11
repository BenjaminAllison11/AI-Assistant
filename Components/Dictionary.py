from Components.Dependencies import query, speak, requests

def define(query):
    if query[0] == 'define':
        query = ' '.join(query[1:])
        definition_response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{query}")
        speak('Getting you a definition')
        if definition_response.status_code == 200:
            definition = definition_response.json()
            meanings = definition[0]['meanings']
            for meaning in meanings:
                definitions = meaning['definitions']
                for definition in definitions:
                    speak(definition['definition'])