#  REMOVE ALL OCCURENCES OF A SPECIFIC ITEM IN A LIST
list= [5,20,15,20,25,50,20]
def remove_from_list(list, val):
    list_updated=[x for x in list if x!= val]
    return list_updated

print ("The output is: ", remove_from_list(list, 20))