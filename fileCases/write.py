#You can write in two ways
#write(str)
#writelines(str)

#e.g

# f= open("wish.txt", "w")
# f.write("Welcome\n")
# f.write("to\n")
# f.write("Python world\n")
# f.close()
# print("Data written successfuly")


#or

f= open("names.txt", "a")
list=["Ramesh\n","vandladh\n","Dami\n","Tobi\n"]
f.writelines(list)
print("list of lines written to file successfully")
