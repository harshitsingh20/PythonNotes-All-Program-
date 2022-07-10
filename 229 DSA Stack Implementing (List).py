# First Method:- By using user input

stack = []

def push():
    if len(stack)==n:
        print("Limit is Full")
    else:
        element = input("Enter the Element: ")
        stack.append(element)
        print(stack)

def pop():
    if stack==0:
        print("Stack is Empty")
    else:
        element=stack.pop()
        print("Removed element",element)
        print(stack)

n=int(input("Select the limit of stack: "))
while True:
    print("Select the operation 1) Push  2) Pop  3) Quit")
    choice=int(input("Enter the Element: "))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("Enter the Correct Operation")


