#Bubble Sort: - Ascending Order
# list1 = [10, 15, 4, 23, 0]
# print("Unsorted List: ", list1)
# for j in range(len(list1)-1):
#     for i in range(len(list1)-1):
#         if list1[i] > list1[i+1]:
#             list1[i], list1[i + 1] = list1[i+1], list1[i]                #Swap
# print("Sorted List: ", list1)       # This will Directly show the Final Result


#If i want to see all the steps in Bubble Sort Ascending Order

# list1 = [10, 15, 4, 23, 0]
# print("Unsorted List: ", list1)
# for j in range(len(list1)-1, 0, -1):
#     for i in range(j):
#         if list1[i] > list1[i+1]:
#             list1[i], list1[i + 1] = list1[i+1], list1[i]                #Swap
#             print(list1)
#         else:
#             print(list1)
#     print()                                                             #It gives the space in the itrations
# print("Sorted List: ", list1)




#Bubble Sort: - Descending Order

# list1 = [10, 15, 4, 23, 0]
# print("Unsorted List: ", list1)
# for j in range(len(list1)-1):
#     for i in range(len(list1)-1):
#         if list1[i] < list1[i+1]:
#             list1[i], list1[i + 1] = list1[i+1], list1[i]                #Swap
# print("Sorted List: ", list1)       #Iteration


#User Input Using Bubble Sort ascending order

list1 = []
num = int(input("How many numbers you want to insert: "))
print("Enter the Value ")
for h in range(num):
    list1.append(int(input()))
print("Unsorted List: ", list1)
for j in range(len(list1)-1, 0, -1):
    for i in range(j):
        if list1[i] > list1[i+1]:
            list1[i], list1[i + 1] = list1[i+1], list1[i]                #Swap
            print(list1)
        else:
            print(list1)
    print()                                                             #It gives the space in the itrations
print("Sorted List: ", list1)