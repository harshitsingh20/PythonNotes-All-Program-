def power(base,exp):
    assert exp>=0 and int(exp) == exp,"Posivive  and  Integer"
    if exp==0:
        return 1
    elif exp==1:
        return base
    else:
        return base * power(base,exp-1)
print(power(2,4))



#
# def pow(base,exp):
#   assert exp>=0 and int(exp)==exp,""
#   if exp==0:
#     return 1
#   if exp==1:
#     return base
#   else:
#     return base * pow(base,exp-1)
#
# num1= int(input("Enter base: " ))
# num2= int(input("Enter exp: "))
#
# print(pow(num1,num2))
