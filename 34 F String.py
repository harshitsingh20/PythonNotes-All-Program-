  #1 String Formatting (% Operator)

name= "Jack"
n= "My name is %s"%name
print(n)
#Output: "My name is Jack."

#2 Using Tuple ()
name="Jack"
classe = 5
s="%s is in class %d"%(name,classe)
print(s)


#3  String Formatting (str.format)

str = "This article is written in {} "
print (str.format("Python"))

#4 Using f-Strings ( f ):

## declaring variables

str1="Python"
str2="Programming"
print(f"Welcome to our {str1}{str2} tutorial")