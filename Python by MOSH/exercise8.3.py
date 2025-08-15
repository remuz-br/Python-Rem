#"converting any emoji words into actual emoji" exercise
def emoji_converter(message): #where also using a function for the exercise
    emojis = {
        'sad': ':(',
        'happy': ':)',
        'angry': '>:(',
        'love': '<3',
        'lol': '😂',
        'cry': '😭',
        'wow': '😮',
        'cool': '😎',
        'sleepy': '😴',
        'ok': '👌',
        'yes': '👍',
        'no': '👎',
        'heart': '❤️',
        'hello': '👋',
        'bye': '👋'
    }
    messagesplit = message.split(' ') #splittin using a space as a seperator a string into a list to access its words one by one
    output = ''

    for word in messagesplit: #the string is now a list so we can access its words
        output += emojis.get(word, word) + ' ' #accessing the dictionary with get while the secondary parameter will return the word without definition and also adding spaces as seen there,

    return output

messages = input('talk to me:')
tester = emoji_converter(messages)
print(tester)