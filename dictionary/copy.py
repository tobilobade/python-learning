

#Write down a program that has a list of trainees, the name should be the full name of the person
#create a dictionary where the initials is the key and the full name is the value

names=["Damilola Adetugboboh", "Tega ramesh hgh", "Michael Jackson"]


#got the names of each of the list (fname)
# split it in two then joined them together taking the first index of the two 
initials_name={"".join([y[0].upper() for y in x.split(" ")]): x for x in names}


print('test', initials_name)