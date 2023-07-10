#CONCATENATE TWO LIST INDEX VALUE
list1=["M","na","I","Ke"]
list2=["y","me","s","lly"]
list3=[]

for i in range(len(list1)): #iterate over the length of first array
    list3.append(list1[i]+list2[i]) #append the new array to the combination of the two indexes  while iterating.
    
print(list3)


#write a program which enters 5 names in a list, sort the list based on string length