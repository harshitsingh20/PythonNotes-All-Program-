# Exersise 5
# Health Management System
# 3 clients - Harshit, Sherya and Simran
# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:              #Clints
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("41 Harshit-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("42 Harshit-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("43 Sherya -ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("44 Sherya-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("45 Simran-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("46 Simran-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(Harshit),2(Sherya),3(Simran)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("41 Harshit-ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif (c == 2):
            with open("42 Harshit-food.txt") as op:
                for i in op:
                    print(i, end=" ")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("43 Sherya-ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif (c == 2):
            with open("44 Sherya-food.txt") as op:
                for i in op:
                    print(i, end=" ")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("45 Simran-ex.txt") as op:
                for i in op:
                    print(i, end=" ")
        elif (c == 2):
            with open("46 Simran-food.txt") as op:
                for i in op:
                    print(i, end=" ")
    else:
        print("plz enter valid input (Harshit,Sherya,Simran)")


print("Health Management System: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for Harshit 2 for Sherya 3 for Simran "))
    take(b)
else:
    b = int(input("Press 1 for Harshit 2 for Sherya 3 for Simran "))
    retrieve(b)