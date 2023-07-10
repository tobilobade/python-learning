#USED TO MANIPULATE THE LIST
item= [900, 800, 1100, 1200,777]


names= map(lambda x :x*2, item)
display_names= list(names)
print(display_names)


even= filter(lambda x: x%2==0, item)
display_even= list(even)
print(display_even)