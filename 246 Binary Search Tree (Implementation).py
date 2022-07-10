# class Binary_search_tree:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
# root = Binary_search_tree(10)
# print(root.data)
# print(root.left)
# print(root.right)

# User Input Binary Search

# def Binary_Search(list1, key):
#     low = 0
#     high = len(list1) - 1
#     temp = False
#     while low<=high and not temp:
#         mid = (low + high) // 2
#         if key == list1[mid]:
#             temp = True
#         elif key > list1[mid]:
#             low = mid + 1
#         else:
#             high = mid - 1
#     if temp == True:
#         print("Key is found")
#     else:
#         print("Key is not found")
#
# list1 = [2,5,6,7,8,2,4,10]
# list1.sort()
# print(list1)
# key = int(input("Enter the number: "))
# Binary_Search(list1,key)


