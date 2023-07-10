def hello_decorator(func):
    def inner1():
        print("Hello, this is before function is executed")
        func()
        print("This is after function is executed")

@hello_decorator
def function_to_be_used():
    print("This is inside function")

function_to_be_used=hello_decorator(function_to_be_used)

function_to_be_used()