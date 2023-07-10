#Write a python program to count repeated characters in a string

# new_array= []
# a = input("input a letter to find the amount of occurences: ")

# new_array.append(a)
# print(new_array[0])


# print(new_array[0] + " ", word.count(new_array[0]))
word = input("Enter your word: ")

for i in range(0, len(word)):  
    count = 1;  
    for j in range(i+1, len(word)):  
        if(word[i] == word[j] and word[i] != ' '):  
            count = count + 1;  
            word = word[:j] + '0' + word[j+1:]


    
    if(count >= 1 and word[i] != '0'):  
        print(word[i],": ",count)



