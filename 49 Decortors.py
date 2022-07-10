# There are two ways to write a Python decorator:
# 1) We can pass our function to the decorator as an argument, thus
# define a function and pass it to our decorator.
# 2) We can simply use the @ symbol before the function we'd like to decorate.

def inner1(func):   #Take function as an aurument
    def inner2():
        print("Before function execution")
        func()
        print("After function execution")
    return inner2

@inner1
def function_to_be_used():
    print("This is inside the function")

function_to_be_used()