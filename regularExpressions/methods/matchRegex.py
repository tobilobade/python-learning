
#match()-used to check the given pattern at the beginning of the target string, if match is seen , we will get a match object otherwise None.

import re 
s= input("Enter pattern to check: ")
m = re.match(s, "abandcefghikjsahhgddgdhdsugf")
if m != None:
    print("match is available at the beginning of the string")
    print ("start index",m.start(), "and end index: ", m.end())
else:
    print("match is not available at beginning of string")  #N.B - only returns the match of the beginning unlike finditer

