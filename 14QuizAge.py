#Input human age if you are grerater than 18 elegable if not your are not elgable

print("Enter your age: ",end="")
age = int(input())
if age>18 and age<101:
    print("you are elegable")
elif age==18:
    print("We think about that")
else:
    print("You are not elegable")