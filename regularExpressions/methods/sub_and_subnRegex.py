import re
# #SUB
# #to target every sting pattern and will be replaced with provided replacement


m = re.sub([a-z], "#", "abaaba")


#SUBN
#displays in a tuple and shows the amount of occurrence


m = re.subn("[a-z]", "#", "a7b0baa8b5a")
print(m)
print('the result of the string is', m[0])
print('the number of replacement',m[1])