def emoji(words):
    words = message.split(' ')
    #print(words)
    emojis = {
        ":)": "😊",
        ":(": "😢"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
final_output = emoji(message)
print(final_output)
