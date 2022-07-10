from array import *

arr1 = array('i',[1,2,3,4,5,6])

def arryElement(array,index):
    if index>=len(array):
        print("Array not found")
    else:
        print(array[index])
arryElement(arr1,3)