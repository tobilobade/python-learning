#FIND VOWEL IN WORD 

#SOLUTION 1{

def vowels (word):
    count= 0
    for letter in word:
        if letter == "a" or letter== "e" or letter== "i" or letter== "0" or letter== "u":
            count+=1
    return count
# }

    #OR

#SOLUTION 2{

value3=input("Enter any word: ")
def vowels (word):
    count= 0
    for letter in word:
        if letter in "aeiou":
            count+=1
    return count

print(vowels(value3))

# }


