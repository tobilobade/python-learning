import re
# #SEARCH
# #search fuction search the given pattern in a string , if found ,it returns match object which represents the first occurence
s= input("Enter pattern to check: ")
m = re.search(s, "abaaba")
if m != None:
    print("Match is available")
    print("first occurenceof match with start index: ", m.start(), "and end index", m.end())
else:
    print("match not available")
