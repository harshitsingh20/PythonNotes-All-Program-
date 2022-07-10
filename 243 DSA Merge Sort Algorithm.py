# Ascending Order

def merge_Sort(list1):
    if len(list1) > 1:                      #Base Condition: - Stopping Condition
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]
        merge_Sort(left_list)               # Recursive Case
        merge_Sort(right_list)              # Recursive Case
        i = 0       #left Side index
        j = 0       #Right Side index
        k = 0       #Where we store the sorted data of list1
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i = i + 1
                k = k + 1
            else:
                list1[k] = right_list[j]
                j = j + 1
                k = k + 1
        while i < len(left_list):
            list1[k] = left_list[i]
            i = i + 1
            k = k + 1
        while j < len(right_list):
                list1[k] = right_list[j]
                j = j + 1
                k = k + 1
num = int(input("How many element you want to insert: "))
list1 = [int(input()) for x in range(num)]
merge_Sort(list1)
print("Sorted list is; ",list1)