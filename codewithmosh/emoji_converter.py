message = input('>')

def emoji_converter(message):
    words = message.split(' ')
    #print(words)

    emojis = {
        ":)": '\U0001F600',
        ":D": '\U0001F603'
    }

    output = ""
    for item in words:
        if emojis.get(item) is not None:
            output += emojis.get(item) + " "
        else:
            output += item + " "
    return output

print(emoji_converter(message))