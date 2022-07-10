# Lambda functions or anonymous functions :It is a one liner function
# def add(a, b):
#     return a+b
#
# # minus = lambda x, y: x-y
#
# def minus(x, y):
#     return x-y
#
# print(minus(9, 4))


a =[[1, 14], [5, 6], [8,23]]
a.sort(key=lambda x:x[1])       # key takes the function as an input
print(a)