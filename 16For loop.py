#For

list1=[["Harshit",1],["Ankit",2],["Anjani",3],["Renu",4]]
for item, lollypop in list1:
    print(item,lollypop)


# Type casting list in tuple

list2=[["Harshit",1],["Ankit",2],["Anjani",3],["Renu",4]]
tuple=tuple(list2)
for item, lollypop in tuple:
    print(item,lollypop)


# Type casting list in Dictionary

list3=[["Harshit",1],["Ankit",2],["Anjani",3],["Renu",4]]
dict=dict(list3)
for item, lollypop in dict.items():
    print(item,lollypop)