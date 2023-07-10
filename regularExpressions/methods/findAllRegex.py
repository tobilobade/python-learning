import  re
# #FIND ALL 
# #to find all occurences ,it will return a list of object which contains all occurences
s= input("Enter pattern to check: ")
m = re.findall(s, "abaaba")
print(m)