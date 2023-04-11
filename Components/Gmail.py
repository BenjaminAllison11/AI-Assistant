from Components.Dependencies import speak, webbrowser, query

def gmail(query):
    if query[0] == 'i' and query[1] == 'need' and query[2] == 'to' and query[3] == 'send' and query[4] == 'an' and query[5] == 'email':
                speak('Bringing up g-mail now')
                webbrowser.open_new('https://mail.google.com/mail/u/0/#inbox?compose=new')