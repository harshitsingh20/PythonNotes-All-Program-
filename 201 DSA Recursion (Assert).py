def factorial(n):
    assert n>=0 and int(n)==n, 'The Number must be Positive and Integer Only '
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# The time complexity of recursive factorial is O(n).

# def fact(n):
#   assert n>=0 and int(n)==n,''
#   if n in [0,1]:
#     return n
#   else:
#     return n * fact(n-1)
#
# number = int(input("Enter the number: "))
# l = list()
# for i in range(number+1):
#   l.append(fact(i))
# for i in reversed(l):
#   print(i)




# 1. Write a Python program to calculate the sum of a list of numbers.

# def list_sum(n):
#     if len(n) == 1:
#         return n[0]
#     else:
#         return n[0] + list_sum(n[1:])
# print(list_sum([1, 4, -1, 6, 7]))


