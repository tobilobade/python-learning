#There are different ways to read a file
# 1) read()- it will read everything and display in front of you
# 2) read(n)- read up to limits provided
# 3) readlines()-read only one line
# 3) readline()-all content


f=open("abc.txt","r")
data=f.readlines()
print(data)
f.close()