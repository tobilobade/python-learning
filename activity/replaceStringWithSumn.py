word=input("Enter your word: ")

def string(word):
    character= word[0]
    string = word.replace(character,"$")
    string = character + string[1:]


    return string


print(string(word))