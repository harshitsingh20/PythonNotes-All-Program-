# num = int(input("Enter the Number of rows: "))
# for i in range(0,num):  #Rows
#     for j in range(0,num-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# Output
#       *
#      * *
#     * * *

# Reverse Pyramid Shape

# num = int(input("Enter the Number of rows: "))
# for i in range(num,0,-1):  #Rows
#     for j in range(0,num-i):
#         print(end=" ")
#     for j in range(0,i):
#         print("*",end=" ")
#     print()

# Output
#     * * *
#      * *
#       *


# Diamond Shape

def dimand(rows):
    for i in range(rows):
        print(' '*(rows-i-1)+'* '*(i+1))
    for j in range(rows-1,0,-1):
        print(' '*(rows-j)+'* '*(j))
dimand(5)