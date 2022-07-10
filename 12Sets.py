# Sets : It takes only unique values
# Empty Set
s=set()
print(type(s))

# Using set with List

s1=set([1,2,3,4,5,])
print(s1)

# Add element in set
# .add()

s2=set()
s2.add(1)
print(s2)

# Union Function:- 	Return a set containing the union of sets
# .union()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

# clear function:- Removes all the elements from the set
# clear()

fruits1 = {"apple", "banana", "cherry"}
fruits1.clear()
print(fruits1)

# Copy Function:- 	Returns a copy of the set
# copy()

fruits2 = {"apple", "banana", "cherry"}
x = fruits2.copy()
print(x)

# difference function :- Returns a set containing the difference between two or more sets
# difference()

x1 = {"apple", "banana", "cherry","mango"}
y = {"google", "microsoft", "apple","mango"}
z = x1.difference(y)
print(z)

# Discard Function:- Remove the specified item
# .discard

fruits3 = {"apple", "banana", "cherry"}
fruits3.discard("banana")
print(fruits3)

# Remove function:- Remove the specified element
# .remove()

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

# Intersection Function:-Return a set that contains the items that exist in both set
# .intersection()

x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}
z2 = x2.intersection(y2)
print(z2)

# Isdisjoint Function:- Return True if no items in set x is present in set y
# .isdisjoint()

x4 = {"apple", "banana", "cherry"}
y4 = {"apple", "microsoft", "facebook"}
z4 = x4.isdisjoint(y4)
print(z4)

# Issubset:- Return True if all items set x are present in set y
# .issubset()

x5 = {"a", "b", "c"}
y5 = {"f", "e", "d", "c", "b", "a"}
z5 = x5.issubset(y5)
print(z5)

# Symmetric_difference Function:- Return a set that contains all items from both sets, except items that are present in both sets
# .symmetric_difference()

x6 = {"apple", "banana", "cherry"}
y6 = {"google", "microsoft", "apple"}
z6 = x6.symmetric_difference(y6)
print(z6)


# POP Function:- Removes an element from the set
# .pop

x7 = {"apple", "banana", "cherry"}
x7.pop()
print(x7)