# Ascending order

# Taking First element pivot
def pivot_place(list, first, last):
    pivot = list[first]
    left = first + 1
    right = last
    while True:
        while left <= right and list[left] <= pivot:
            left = left + 1
        while left <= right and list[right] >= pivot:
            right = right - 1
        if left > right:
            break
        else:
            list[left], list[right] = list[right], list[left]
    list[first], list[right] = list[right], list[first]  # Taking First element pivot : - Always swap to right
    return right    #In this Place pivot element is present

def devide_Conquer(list, first, last):
    if first < last:
        p = pivot_place(list, first, last)  # This is the function class      #It will hold the return result
        devide_Conquer(list, first, p - 1)  # 0 to pivort element
        devide_Conquer(list, p + 1, last)  # pivort to last element

list = [56, 26, 93, 17, 31, 44]
devide_Conquer(list, 0, len(list)-1)
print(list)




# Ascendng order

# Taking Last element pivot
# def pivot_place(list, first, last):
#     pivot = list[last]
#     left = first
#     right = last - 1
#     while True:
#         while left <= right and list[left] <= pivot:
#             left = left + 1
#         while left <= right and list[right] >= pivot:
#             right = right - 1
#         if left > right:
#             break
#         else:
#             list[left], list[right] = list[right], list[left]
#     list[last], list[left] = list[left], list[last]  # Taking First element pivot : - Always swap to right
#     return left    #In this Place pivot element is present
#
# def devide_Conquer(list, first, last):
#     if first < last:
#         p = pivot_place(list, first, last)  # This is the function class      #It will hold the return result
#         devide_Conquer(list, first, p - 1)  # 0 to pivort element
#         devide_Conquer(list, p + 1, last)  # pivort to last element
#
# list = [56, 26, 93, 17, 31, 44]
# devide_Conquer(list, 0, len(list)-1)
# print(list)



# Random Element Import
# Ascending Order

import random


def pivot_place(list, first, last):
    random_index = random.randint(first, last)
    list[random_index], list[first] = list[first], list[random_index]

    pivot = list[first]
    left = first + 1
    right = last
    while True:
        while left <= right and list[left] <= pivot:
            left = left + 1
        while left <= right and list[right] >= pivot:
            right = right - 1
        if left > right:
            break
        else:
            list[left], list[right] = list[right], list[left]
    list[first], list[right] = list[right], list[first]  # Taking First element pivot : - Always swap to right
    return right    #In this Place pivot element is present

def devide_Conquer(list, first, last):
    if first < last:
        p = pivot_place(list, first, last)  # This is the function class      #It will hold the return result
        devide_Conquer(list, first, p - 1)  # 0 to pivort element
        devide_Conquer(list, p + 1, last)  # pivort to last element

list = [56, 26, 93, 17, 31, 44]
devide_Conquer(list, 0, len(list)-1)
print(list)
