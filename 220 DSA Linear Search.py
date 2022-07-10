# Using For Loop

# Example 1

# def LinearSearch(list1,key):
# 	for i in range(len(list1)):
# 		if key == list1[i]:
# 			print("Element is Found at the index of: ",i)
# 			break
# 	else:
# 		print("Element is not Found")
#
# list1 = [1,2,3,4,5,6,7,8,9,10]
# key = int(input('Enter the number: '))
# LinearSearch(list1,key)


# Example 2

# pos = -1
# def search(list, n):
#  for i in range(len(list)):
#   if list[i]==n:
#    globals()['pos'] = i
#    return True
#  return False
#
# list = [5,8,4,6,9,2]
# n = 9
#
# if search(list, n):
#  print("Found at ",pos)
# else:
#  print("Not Found")


# Print the dublicate in linear Search using for loop

# def LinearSearch(list1, key):
# 	list2 = []
# 	flag = False
# 	for i in range(len(list1)):
# 		if key == list1[i]:
# 			flag = True
# 			list2.append(i)
# 	if flag == True:
# 		print("Element is Found at the index of: ")
# 		for i in list2:
# 			print(i)
# 	else:
# 		print("Element is not found")
#
# list1 = [1,2,3,1,4,5,9,6,7,8,9,10]
# print(list1)
# key = int(input('Enter the number: '))
# LinearSearch(list1, key)


# Using While Loop

pos = -1
def search(list, n):
    i = 0
    while(i<len(list)):
        if list[i]==n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False

list = [5,8,4,6,9,2]
n = 9

if search(list, n):
 print("Found at ",pos)
else:
 print("Not Found")



# Print the dublicate in linear Search using while loop

# def linearSearch(list1, key):
# 	i=0
# 	flag = False
# 	list2 = []
# 	while i<len(list1):
# 		if list1[i] == key:
# 			flag = True
# 			list2.append(i)
# 		i = i + 1
# 	if flag == True:
# 		print("Element is Found at the index of: ",i)
# 		for i in list2:
# 			print(i)
# 	else:
# 		print('Element is not Found')
# list1 = [10, 20, 80, 30, 60, 50,110, 100, 130, 170, 10]
# key = int(input("Enter the key: "))
# linearSearch(list1,key)