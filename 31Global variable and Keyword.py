#local Variable

def sum():
    a = 10  # local variable cannot be accessed outside the function
    b = 20
    sum = a + b
    print(sum)
sum()


#Gloable Variable

h=1  #global variable

def print_Number():

            c=h+1;
            print(c)
print_Number()


#Nested function

def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

harry()
print(x)
