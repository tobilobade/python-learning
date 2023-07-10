import re 
#some popular regex syntax for characters

#[abc]- either a or b or c
#[^abc]-except a and b and c
#[a-z]- any lower case alphabet symbol
#[A-Z]- any upper case alphabet symbol
#[a-zA-Z]- any alphabet symbol
#[0-9]- any digit from 0 to 9
#[a-zA-Z0-9]- Any Alphanumeric
#[^a-zA-Z0-9]- without Any Alphanumeric(special characters)


#PREDIFINED CHARACTERS
#\s- Space Characters
#\S- any character except space Characters
#\dd-any digit 0-9
#\D any character except Digit
#\w- any character and number except special
#\W- any character including special characters




#searching for the pattern of uppercase
# matcher=re.finditer("[A-Z]", "a7b@k9z")
# for match in matcher:
#     print (match.start(),"...",match.group())


# #searching for the pattern of digits
# matcher=re.finditer("\d", "a7b@k9z")
# for match in matcher:
#     print (match.start(),"...",match.group())


matcher=re.finditer("a{2,4}", "abaabaaaba")
for match in matcher:
    print (match.start(),"...",match.group())