#CREATE A STRING MADE OF THE MIDDLE THREE CHARACTERS

str1="JhonDipPeta" 
str2="JaSonAy"

def getString(character):
    mid= int(len(character)/2) #divide the length of the argument(string) that will be converted to an int into two

    ans= character[mid-1:mid+2] #slice 
    print("The three middle characters are: ", ans)

getString(str1)
getString(str2)