# Variables:- A variable is a name given to any storage area or memory location in a program.
# we cannot give the start the variable by these symbols:- $,-,%,@, and any function name
var1 = "Hello Harshit "      # String Type variable

print(var1)

var2 = 40       # Integer Type variable
print(var2)

var3 = 56.5     # Float Type variable
print(var3)

# Type Function : is used to tell which type of variable is it

print(type(var1))
print(type(var2))
print(type(var3))
"""
Data Types in Python
Primarily there are following data types in Python.

1)Integers (<class 'int'>): Used to store integers
2)Floating point numbers (<class 'float'>): Used to store decimal or floating-point numbers
3)Strings (<class 'str'>): Used to store strings
4)Booleans (<class 'bool'>): Used to store True/False type values
5)None:- None is a literal to describe 'Nothing' in Python 

String literals:- A string literal is a sequence of characters surrounded by quotes. We can use both single, double, 
or triple quotes for a string.
"""

# Concatenation :- is used to add same type of data types

var4 = "How are you"
print(var1 + var4)

# Type casting Function :- is used to switch from variables
#1) str()
#2) int()
#3) float()

var5="50"
var6="60"
print(type(var6))
print(type(var5))
print(int(var5)+int(var6))

# If you want to print a string many times so use

var7="Singh is king "
print(10*(var7))

# User Input :- input() function

print("Enter the number ")
num1 = input()
print("you enter this number:\n",int(num1)+40)



# Important Questions

# 1) print(type(0xFF))

# Output:- Int

# 2) print(type({}) is set)

# Output:- False

# 3) print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

# Output:- False True True True

# 4) In Python 3, what is the type of type(range(5))

# Output:- Range