from array import *
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

del T[3][0]
print(T)

def Del(arrr1):
    for i in arrr1:
        for r in i:
            print(r,end=" ")
        print()
Del(T)