import re
#fullmatch()
# we can use fullmatch() function  to matcha pattern to all of target string i.e if the complete string should be matched accorden to given pattern
s= input("Enter pattern to check: ")
m = re.fullmatch(s, "abab")
if m != None:
    print("full string matched")
else:
    print("full string NOT matched")
