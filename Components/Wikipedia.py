from Components.Dependencies import wikipedia, speak, query


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

def wikipedia(query):
    if query[0] == 'wikipedia':
        query = ' '.join(query[1:])
        speak('Browsing Wikipedia for your information')
        speak(search_wikipedia(query))
