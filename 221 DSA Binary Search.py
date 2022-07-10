# Binary Search:- In this case all the values(Array) has to be sorted

# Example 1
#
# def BinarySearch(list1, key):
# 	low = 0
# 	high = len(list1)-1
# 	Found = False
# 	while low <= high and not Found:
# 		mid = (low + high) // 2
# 		if key == list1[mid]:
# 			Found = True
# 		elif key > list1[mid]:
# 			low = mid + 1
# 		else:
# 			high = mid - 1
# 	if Found==True:
# 		print("Key is Found")
# 	else:
# 		print("Key is not Found")
# list1 = [11,23,3,44,5,36,7,8,9,10]
# list1.sort()
# print(list1)
# key = int(input("Enter the value of key: "))
# BinarySearch(list1, key)


# Example 2


pos=-1

def Binary(list, n):
    l = 0   #Lower Bond
    u = len(list)-1 # Upper Bond
    while l<=u:
        mid = (l+u)//2  #Double slash gives the integer value
        if list[mid]==n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l=mid+1
            else:
                u=mid-1

list = [5,8,4,6,9,2]
n = 9

if Binary(list, n):
 print("Found at ",pos+1)
else:
 print("Not Found")