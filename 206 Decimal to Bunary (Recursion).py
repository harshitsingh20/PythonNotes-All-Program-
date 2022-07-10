def decimalToBinary(n):
    assert int(n)==n,"Number Should br Integer"
    if n==0:
        return 0
    else:
        return int(n%2) + 10 * decimalToBinary(int(n/2))
print(decimalToBinary(13000))


# Important Questions

# 1) Write a Python program to calculate the sum of a list of numbers.
#
# def sum_of_List(n):
#     if len(n) == 1:
#         return n[0]
#     else:
#         return n[0] + sum_of_List(n[1:])
# print(sum_of_List([1,2,3,4,5]))


# 2) Write a Python program to calculate the geometric sum of n-1
#
# def fac(n):
#     if n < 0:
#         return 0
#     else:
#         return 1 / (pow(2,n)) + fac(n-1)
#
# print(fac(7))

# 3 Write a Python program to calculate the harmonic sum of n-1.

# def harmonic(n):
#     if n < 2:
#         return 1
#     else:
#         return 1 / n + (harmonic(n-1))
# print(harmonic(7))