# add the total items of each array using comprehensive list
from functools import reduce
d= [123, 475, 333, 111]

sum=[reduce(lambda x,y:int(x)+int(y), str(z)) for z in d ]
print (sum)