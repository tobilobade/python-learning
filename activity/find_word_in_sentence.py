
#TO FIND WORD IN SENTENCE

value2=input("Enter any sentence: ")
value3=input("Enter any word: ")

def vowels (sentence, word):     
    if word in sentence:
        return True
    else:
        return False 

x = vowels(value2, value3)
if x:
    print("found")
else:
    print ("not found")