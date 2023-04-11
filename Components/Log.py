from Components.Dependencies import speak, datetime, parseCommand, query
def log(query):
    if query[0] == 'log':
                speak('Ready to record your notes')
                newNote = parseCommand().lower()
                now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                with open('note_%s.txt' % now, 'w') as newFile:
                    newFile.write(newNote)
                speak('Note written')