#(Ascending Order)

list1 = [56, 3, 2, 78, 6, 0]
for i in range(len(list1)):
    min_val = min(list1[i:])                    # This gives the minium value in list
    min_Index = list1.index(min_val)
    list1[i], list1[min_Index] = list1[min_Index], list1[i]
print(list1)



# (Descending Order)

# list1 = [56, 3, 2, 78, 6, 0]
# for i in range(len(list1)):
#     min_val = max(list1[i:])                    # This gives the minium value in list
#     min_Index = list1.index(min_val)
#     list1[i], list1[min_Index] = list1[min_Index], list1[i]
# print(list1)



# This Code Gives the minium value in first index and swap it (Ascending Order).

# min_val = min(list1)                    # This gives the minium value in list
# min_Index = list1.index(min_val)
# list1[0], list1[min_Index] = list1[min_Index], list1[0]