import numpy as np

arr1 = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
#print(arr1)

newArr1 = np.insert(arr1,0,[[1,2,3,4]],axis=0)
print(newArr1)

newArr1 = np.append(arr1,[[5,6,7,8]],axis=0)
print(newArr1)