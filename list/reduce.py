#IT IS USED TO ADD ALL ELEMENTS IN A LIST
from functools import reduce
items= [111,222,333,444]
cost= reduce(lambda x,y:y-x,items)
print(cost)