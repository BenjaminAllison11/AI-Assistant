from Components.Dependencies import speak, webbrowser, query


def websearch(query):
    if len(query) >= 2 and query[0] in ['go', 'look', 'search'] and query[1] in ['to', 'for', 'up']:
                if query[1] == 'to':
                    #use query to go to a site
                    speak('Opening browser...')
                    query = ' '.join(query[2:])
                    webbrowser.open_new(query)
                else:
                    speak('Searching...')
                    query = ' '.join(query[2:])
                    webbrowser.open_new('https://www.bing.com/search?q=' + query)