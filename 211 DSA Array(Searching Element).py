from array import *

arr1 = array('i',[1,2,3,4,5,6])

def searchArry(array,value):
    for i in array:
        if i == value:
            return array.index(value)
    return "Element does not exist"
print(searchArry(arr1,2))