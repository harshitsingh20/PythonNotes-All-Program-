#Faulty calculator

print("Enter the First Number: ",end="")
n1=int(input())
print("Enter the Second Number: ",end="")
n2=int(input())
print("Select the Operators  + ,-,*,/,% ")
n3=input()
if n1==45 and n2==3 and n3=='*':
    print("555")
elif n1==56 and n2==9 and n3=='+':
    print("77")
elif n1==56 and n2==6 and n3=='/':
    print("4")
elif n3=='+':
    summ=n1+n2
    print(summ)
elif n3=='-':
    subb=n1-n2
    print(subb)
elif n3=='*':
    Mul=n1*n2
    print(Mul)
elif n3=='/':
    div=n2/n1
    print(div)
elif n3=='%':
    per=n2%n1
    print(per)
else:
    print("Invalid Input")