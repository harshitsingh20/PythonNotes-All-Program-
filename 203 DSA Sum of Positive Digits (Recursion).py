def sum_fo_digits(n):
    assert n>=0 and int(n)==n,"Positve amd Integer"
    if n==0:
        return 0
    else:
        return int(n%10)+sum_fo_digits(int(n/10))
print(sum_fo_digits(1234))


#Iterative Method


# num = int(input("Enter the Number: "))
# result = 0
# while num>0:
#     digit = num%10
#     result = result + digit
#     num = num//10
# print(result)