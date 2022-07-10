def fibonacci(n):
    assert n>=0 and int(n)==n,"Number Should be Posivive and Integer"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

number=int(input("Enter the Number : "))
print(fibonacci(number))


# Iterative method


# n = int(input("Enter the number: "))
# first = 0
# second = 1
# for i in range(n+1):
#     print(first,end=" ")
#     temp = first
#     first = second
#     second = temp + second



#Reversed

# def fibonacci(n):
#     assert n>=0 and int(n)==n,"Number Should be Posivive and Integer"
#     if n in [0,1]:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# number=int(input("Enter the Number : "))
# l = list()
# for i in range(number):
#     l.append(fibonacci(i))
# for i in reversed(l):
#     print(i,end=" ")