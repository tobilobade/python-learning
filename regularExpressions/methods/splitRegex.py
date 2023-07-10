import re
#SPLIT METHOD
#Split() function is used when we want to split the given target string according to a particular pattern,returns a list of all tokens
m = re.split(",", "KGF,BB1,BB2")
print(m)
for i in m:
    print(i)