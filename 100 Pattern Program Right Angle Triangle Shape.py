# num = int(input("Enter the Number of rows: "))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# Reverse Right Angle Triangle Shape

num = int(input("Enter the Number of rows: "))
for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()
# Output
# * * *
# * *
# *



# Print Odd Numbers of star in our column

# num = int(input("Enter the Number of rows: "))
# h = 1
# for i in range(1,num+1):
#     for j in range(1,h+1):
#         print("*",end=" ")
#     h = h + 2
#     print()
# Output
# *
# * * *
# * * * * *
# * * * * * * *