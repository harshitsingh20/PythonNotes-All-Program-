# Map Function:- A map function executes certain instructions or functionality
# provided to it on every item of an iterable.

# Syntax:- map(function, iterable)          # (Kay apply karna chahate ha, Kaha per apply karna chahater ha)

items = [1, 2, 3, 4, 5]
a=list(map((lambda x: x * x), items)) #Using Lambda Function
print(a)
#Output: [1, 8, 27, 64, 125]


def sq(a):
     return a*a

num = [2,3,5,6,76,3,3,2]
square = list(map(sq, num))     #Without Using Lambda Function
print(square)


numbers = ["3", "34", "64"]     #Convert String Into Int
numbers = list(map(int, numbers))
for i in range(len(numbers)):       #Normal Conversion
    numbers[i] = int(numbers[i])
numbers[2] = numbers[2] + 1
print(numbers[2])



# Suare and Cube Method

def square(a):
    return a*a
def cube(a):
    return a*a*a
func = [square, cube]
numm = [2,3,5,6,76,3,3,2]
for i in range(len(numm)):
    val = list(map(lambda x:x(i), func))
    print(val)

# Filter Function:-  filter function in Python tests a specific user-defined condition for a
# function and returns an iterable for the elements and values that satisfy the condition
# or, in other words, return true.

#Syntax:- filter(function, iterable)

list_1 = [1,2,3,4,5,6,7,8,9]
def is_greater_5(num):
    return num>5
gr_than_5 = list(filter(is_greater_5, list_1))      #List
print(gr_than_5)


a = [1,2,3,4,5,6]
b = [2,5,0,7,3]
c= list(filter(lambda x: x in a, b))        #Using Lambda function
print(c) # prints out [2, 5, 3]


# Reduce Function:- Reduce functions apply a function to every item of an iterable and gives
# back a single value as a resultant

# Syntax:- reduce(function, iterable)

from functools import reduce

list11 = [1,2,3,4,2]
numbb = reduce(lambda x,y:x*y, list11)
# num = 0
# for i in list1:
#     num = num + i
print(numbb)