var1 =55
var2 =60
print("Enter the Number: ")
var3 =int(input())
if var3 > var1:
    print("Greatest")
elif var3==var1:
    print("Equal")
else:
    print("Smallest")


# if else using in list
# in key word

L1 =[3,6,8,9,4,42]
if 6 in L1:
    print("Yes it is the list")
else:
    print("Not present")

# not in key word

L2 =[3,6,8,9,4,42]
if 16 not in L2:
    print("Yes it not the list")
else:
    print("present")