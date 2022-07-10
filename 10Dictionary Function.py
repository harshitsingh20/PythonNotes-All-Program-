# Dictionary
# These are case sensetive
# Dictionaries are written with curly brackets {} , and have keys and values(items)
# This cannot be mutable like List

d0 = {"Harshit":"Non-Veg","Ayush":"veg"}
print(d0)

# If i want to know what Harshit Eat

print(d0["Harshit"])

# Dictionary Inside the Dictionary

d1 = {"Harshit":"Non-Veg","Ayush":"veg","Mayank":{"B":"Bread","L":"Roti"}}
print(d1["Mayank"]["L"])

#To add something in the Dictionary

d2 = {"Harshit":"Non-Veg","Ayush":"veg"}
d2["Mayank"]="Junk Food"
print(d2)

#To delete Something(Item) in the dictionary
# del Function

d3 = {"Harshit":"Non-Veg","Ayush":"veg"}
del d3["Ayush"]
print(d3)

# Copy Function
# .copy()
# It's helps to save the copy to the another dictionary

d4 = {"Harshit":"Non-Veg","Ayush":"veg","Krishna":"Junk Food"}
d5 = d4.copy()
del d5["Krishna"]
print(d4)

# Get Function
# .get()
# It will give the value

print(d4.get("Harshit"))

# Update Function
# .update()
# To add items in the Dictionary

d6 = {"Harshit":"Non-Veg","Ayush":"veg","Krishna":"Junk Food"}
d6.update({"Asma":"Dic"})
print(d6)

# Key Function
# keys()
# To print all the keys in the Dictionary

d7 = {"Harshit":"Non-Veg","Ayush":"veg","Krishna":"Junk Food"}
print(d7.keys())

# Items Function
# items()
# To print all the items in the Dictionary

print(d7.items())


# fromkeys (iterable, value):- List to dictionary this is the method

# list1 = [1,2,3,4,5]
# a = dict.fromkeys((list1) , (10))
# print(a)

# Using range Function

p = dict.fromkeys((range(1,7)), (10))
print(p)


# setdefault():- It is the method, it check for the key, if key is present it gives the value otherwise it gives none and
# add that value to the dictionary

#Syntax

# setdefault(kay, value)

kl = {"Harshit":"Non-Veg","Ayush":"veg"}
z = kl.setdefault(('Aman'), (20))
print(z)
print(kl)