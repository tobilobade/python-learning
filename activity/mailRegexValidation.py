
#Write a python program to check whether the given email is a valid one or not
s=input("Enter email: ")
m= re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
if m!=None:
    print("valid mail")
else:
    print("invalid email")