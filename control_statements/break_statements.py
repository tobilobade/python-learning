group=[1,2,3,4]
search= int(input("enter number: "))
for element in group:
    if search==element:
        print("element found in group")
        break
    else:
        print("not found")
        
