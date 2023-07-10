#FIND THE LARGEST ITEM FROM A GIVEN LIST USING LIST COMPREHENSION
x=[4,6,8,24,12,2]

max= max(x)

largest_num=[max for numbers in range(x.count(max))]
print(largest_num)