def emoji_converter(message):
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
    messagesplit = message.split(' ')
    output = ''

    for word in messagesplit:
        output += emojis.get(word, word) + ' '

    return output

messages = input('talk to me:')
tester = emoji_converter(messages)
print(tester)