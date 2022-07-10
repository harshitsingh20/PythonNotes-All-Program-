# We make function by using def function
# Normal function

a=30
b=40
c=sum([a,b]) #Built in function
print(c)


# Without Input value in Function
def function1():
    print("Hello Welcome to Function 1")
function1()


#Taking input in Function
def function2(a,b):
    print("Hello Welcome to Function 2",a+b)
function2(5,7)

# Store value in function in third variable

def function3(a,b):
    """This is a function which will calculate average of two numbers
        this function doesnt work for three numbers"""
    average=(a+b)/2
    return average
h=function3(5,7)
print(h)
print(function3.__doc__)#This is the DocString:-This us used after the next line of function