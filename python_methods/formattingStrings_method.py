#TO FORMAT THE STRINGS DYNAMICALLY
# BY USING .FORMAT() 
name="Rakesh"
salary=10
age=18
name2= "Dami"
print("{}'s salary is {} and his age is {}".format(name,salary,age))
print("{0}'s salary is {1} and his age is {2}".format(name,salary,age))
print("{x}'s salary is {y} and his age is {z}".format(x=name2,y=salary,z=age)) #YOU CAN EXCHANGE ANY VARIABLE OF YOUR CHOICE

#TO CONCATENATE WITH F-STRING
# BY USING F-string 
name="John"
message= f'Hi {name}' #THIS ACTS LIKE `{HI JOHN}` IN JAVASCRIPT
print(message)