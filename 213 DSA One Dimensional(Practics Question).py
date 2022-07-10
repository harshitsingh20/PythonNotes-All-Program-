from array import *

#1) Create of travrese.

print("Step one")
arr1 = array('i',[1,2,3,4,5,6])
for i in arr1:
    print(i)

# 2) Access individual elements through indexes.

print("Step two")
print(arr1[0])

# 3) Append any value to array

print("Step three")
arr1.append(7)
print(arr1)

# 4) Insert values in array

print("Step four")
arr1.insert(0,0)
print(arr1)

# 5) Extend Python array

print("Step Five")
arr2 = array('i',[11,12,13,14,15])
arr1.extend(arr2)
print(arr1)

# 6) Add items from list using fromList() method:-Add List to Array

print("Step Six")
l = [20,21]
arr1.fromlist(l)
print(arr1)

# 7) Remove any array element

print("Step Seven")
arr1.remove(20)
print(arr1)

# 8) Remove last array element

print("Step Eight")
arr1.pop()
print(arr1)

# 9) Fetch any array element using index() method

print("Step Nine")
print(arr1.index(2))

# 10) reverse the array

print("Step Ten")
arr1.reverse()
print(arr1)

# 11) Get array buffer information through buffer_info() method:-Gives the memory Location Number and total
# number of element present in array

print("Step Eleven")
print(arr2.buffer_info())

# 12)Check the number occurrence using count() method

print("Step twelve")
print(arr1.count(15))

# 13)Convert array into string tostring() method

print("Step Thirteen")

# 14) convert array to a python list with same element using tolist() method

print("Step Fourteen")
print(arr1.tolist())

# 15) Append a string to char array using fromstring() method

print("Step Fifteen")

# 16) Slice element from an array
print("Step Sixteen")
print(arr1[1:2])

# Link = https://www.w3resource.com/python-exercises/array/


# Write a Python program to create an array of 5 integers and display the array items. Access individual element through
# indexes.
#
# from array import*
# arr1=array('i',[1,3,5,7,9])
# def soe(arry):
#     for i in arry:
#         print(i)
# soe(arr1)
# print("Access first three items individually")
# print(arr1[0])
# print(arr1[1])
# print(arr1[2])


# Write a Python program to append a new item to the end of the array.
#
# from array import *
# abc=array('i', [1, 3, 5, 7, 9])
# abc.append(11)
# print(abc)


# Write a Python program to reverse the order of the items in the array.
#
# from array import *
# har = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# har.reverse()
# print(har)


# Write a Python program to get the length in bytes of one array item in the internal representation.
#
# from array import *
# ank = array('i', [1, 3, 5, 7, 9])
# har = len(ank)
# print(har)


# Write a Python program to get the current memory address and the length in elements of the buffer used to hold
# an array's contents and also find the size of the memory buffer in bytes.
#
# from array import *
# ppl = array('i', [1, 3, 5, 7, 9])
# print(ppl.buffer_info())


# Write a Python program to get the number of occurrences of a specified element in an array.
#
# from array import *
# uil = array('i', [1, 3, 5, 3, 7, 9, 3])
# print(uil.count(3))


# Write a Python program to append items from inerrable to the end of the array.
#
# from array import *
# ssd = array('i', [1, 3, 5, 7, 9])
# klu = array('i', [1, 3, 5, 7, 9, 1, 3, 5, 7, 9])
# ssd.extend(klu)
# print(ssd)


# Write a Python program to convert an array to an array of machine values and return the bytes representation
#
# from array import *
# x = array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
# s = x.tobytes()
# print(s)


# Write a Python program to append items from a specified list.
#
# from array import *
# asd = array('i',[77,88])
# aas = [1, 2, 6, -8]
# asd.fromlist(aas)
# print(asd)


# Write a Python program to insert a new item before the second element in an existing array.
#
# from array import *
# wqe = array('i', [1, 3, 5, 7, 9])
# wqe.insert(1,4)
# print(wqe)



# Write a Python program to remove a specified item using the index from an array.
#
# from array import *
# qqq = array('i', [1, 3, 5, 7, 9])
# qqq.remove(3)
# print(qqq)


# Write a Python program to remove the first occurrence of a specified element from an array.
#
# from array import *
# rrt = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# rrt.remove(3)
# print(rrt)


# Write a Python program to convert an array to an ordinary list with the same items.
#
# from array import *
# axc = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# ass=axc.tolist()
# print(ass)



# Write a Python program to find whether a given array of integers contains any duplicate element. Return true if
# any value appears at least twice in the said array and return false if every element is distinct
#
# def Duplicate(array):
#     wer = set(array)
#     return len(array) != len(wer)
# print(Duplicate([1,2,3,4,5]))
# print(Duplicate([1,2,3,4,4]))
# print(Duplicate([1,1,2,2,3,3,4,4,5]))



# Write a Python program to find the first duplicate element in a given array of integers. Return -1 If there are
# no such elements.

# def find_first_duplicate(nums):
#     num_set = set()
#     no_duplicate = -1
#     for i in range(len(nums)):
#         if nums[i] in num_set:
#             return nums[i]
#         else:
#             num_set.add(nums[i])
#     return no_duplicate
# print(find_first_duplicate([1, 2, 3, 4, 4, 5]))
# print(find_first_duplicate([1, 2, 3, 4]))
# print(find_first_duplicate([1, 1, 2, 3, 3, 2, 2]))



# Write a Python program to get the array size of types unsigned integer and float.


# from array import *
# arrq = array('I',[20,5,0,80,70,56])
# print(arrq.itemsize)
# azx = array('f',[20.0,10.0,90.8])
# print(azx.itemsize)


