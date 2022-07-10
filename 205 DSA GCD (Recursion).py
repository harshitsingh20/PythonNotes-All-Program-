 # This is also knows as HCF

def gcd(a,b):   # b is reminder
    assert int(a)==a and int(b)==b,"Number Should be Integers"
    if a<0:
        a = -1 * a
    elif b<0:
        b = -1 * b
    elif b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(48,18))


# With the help of Modules

# import math
# a=math.gcd(48,18)
# print(a)


# LCM :- Lowest common Multiple

# def Compute_LCM(num1, num2):
#     if num1 > num2:
#         higher = num1
#     else:
#         higher = num2
#     value = higher
#
#     while True:
#         if higher % num1 == 0 and higher % num2 == 0:
#             print("LCM of ", num1, " and ", num2, " is ", higher)
#             break
#         else:
#             higher = higher + value
#
# num1 = int(input("Enter First the Number: "))
# num2 = int(input("Enter Second the Number: "))
#
# print(Compute_LCM(num1, num2))