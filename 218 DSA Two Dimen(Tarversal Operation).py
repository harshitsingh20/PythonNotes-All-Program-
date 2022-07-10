from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
def har(arr1):
    for r in arr1:
        for c in r:
            print(c,end = " ")
        print()
har(T)