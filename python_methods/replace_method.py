#THIS METHOD IS USE TO REPLACE CONTENTS IN A WORD
# BY USING THE .replace()

course = "Python Programming language"
second_course= course.replace("Python", "Java")  #it replaces python with Java
print(course)
print(second_course)

print(id(course))
print(id(second_course))  #It gives a new memory for the replacement