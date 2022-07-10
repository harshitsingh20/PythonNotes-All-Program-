 # List
# It is used to store multiple items. List are created using squaure brackets []

School = ["Teachers" , "Students" , "Staff Members" , "Principal" , "Vice principal"]
print(School)

# Mix List
# Numbers + String

Schools = ["Teachers" , "Students" , "Staff Members" , "Principal" , "Vice principal", 80, 90]
print(Schools)

# Using Index in List
# Index start with zero

Schoolss = ["Teachers" , "Students" , "Staff Members" , "Principal" , "Vice principal"]
print(Schoolss[4])

# Sort Function in List : - .sort()

Li = [3, 8, 4, 5, 0]
Li.sort()
print(Li)

# Reverse Function in List :- .reverse()

Lii = [3, 8, 4, 5, 0]
Lii.reverse()
print(Lii)

# Slicing in List [ : ]

L = [5, 7, 2, 9, 8]
print(L[0:4])

# Extended Slicing in List

A = [2, 7, 9, 11, 3]
print(A[0:5:2])

# Max in List

Aa = [2, 7, 9, 11, 3]
print(max(Aa))

# Min in List

Ab = [2, 7, 9, 11, 3]
print(min(Ab))

# Append Function in List
# .append()
# To add something the the List in the end

Ac = [2, 7, 9, 11, 3]
Ac.append(4)
print(Ac)

# Insert Function in List
# .insert
# To add something in the List  but always aks which place i have to insert the number

z = [9, 8, 1, 5, 4, 7]
z.insert(2, 6)
print(z)

# Remove Function
# .remove()

q = [3,8,9,0,6,5]
q.remove(9)
print(q)

# Pop Function
# .pop()
# To remove index in the list

e = [5,5,7,8,90,13,3]
e.pop()
print(e)

# Copy Function
# .copy
# The copy() method returns a copy of the specified list.

fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)

# Count Function
# .count
# The count() method returns the number of elements with the specified value.

fruits1 = ["apple", "apple", "banana", "cherry"]
x = fruits1.count("apple")
print(x)

# Extend Function
# .extend()
#The extend() method adds the specified list elements (or any iterable) to the end of the current list

fruits2 = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits2.extend(cars)
print(fruits2)

# Index function
# .index()
# The index() method returns the position at the first occurrence of the specified value.

fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)





# Important Questions

# 1. Check if a list contains an element

# li = [1,2,3,'a','b','c']
# har = 'a' in li
# print(har)
#=> True


# 2. How to iterate over 2+ lists at the same time

# Zip in list

# name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
# animal = ['Cat', 'Dog', 'Fish', 'Goat']
# age = [1, 2, 2, 6]
# z = zip(name, animal, age)
# for name,animal,age in z:
#     print("%s the %s is %s" % (name, animal, age))


# 3. Do python lists store values or pointers?

# Python lists don’t store values themselves. They store pointers to values stored elsewhere in memory.
# This allows lists to be mutable.

# Id in List

# li = [1,2,3,'a','b','c']
# print(id(li))


# 4. What does “del” do?

# a = ['w', 'x', 'y', 'z']
# del a[1]
# #=> ['w', 'y', 'z']


# 5. Remove duplicates from a list

# li = [3, 2, 2, 1, 1, 1]
# list(set(li))
# #=> [1, 2, 3]


# 6. Find the index of the 1st matching element

# fruit = ['pear', 'orange', 'apple', 'grapefruit', 'apple', 'pear']
# fruit.index('apple') #=> 2
# fruit.index('pear') #=> 0


# 7. Remove all elements from a list

# fruit = ['pear', 'orange', 'apple']
# fruit.clear()
# print( fruit )

# OR

# del fruit[:]
# # print( fruit )


# 8. How to manipulate every element in a list with list comprehension

# li = [0,25,50,100]
# [i+1 for i in li]
#=> [1, 26, 51, 101]


# 9. How to deep copy a list?

# For this we need to import the copy module, then call copy.deepcopy().





# 10. How to check if an element is not in a list?

# li = [1,2,3,4]
# 5 not in li #=> True
# 4 not in li #=> False



