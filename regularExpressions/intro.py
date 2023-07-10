#Regular expressions is a sequence of characters that define a search pattern in theoretical C.S and formal language

import re
count= 0
pattern=re.compile("ab")#find the pattern you'd like to recognise
matcher= pattern.finditer("abaababa")
for match in matcher:
    count+=1
    print(match.start(),"...",match.end(),"...",match.group())
    print("The number of occurence is: ", count)