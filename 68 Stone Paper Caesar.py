import random
lis1=['S','P','C']
chance=10
no_of_chance=0
computer_Points=0
human_Points=0
print(" \t \t \t \t Stone,paper,Caesar Game\n \n")
print("S for Stone \nP for Paper \nC for Caesar \n")
while no_of_chance<chance:
    n=input("stone,paper,Caesar\n").upper()
    ran=random.choice(lis1)
    if n==ran:
        print("Tie Both 0 point to each \n ")
    elif n=="S" and ran=="P":
        computer_Points=computer_Points+1
        print(f"your guess {n} and computer guess is {ran} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_Points} and your point is {human_Points} \n ")
    elif n=="S" and ran=="C":
        human_Points=human_Points+1
        print(f"your guess {n} and computer guess is {ran} \n")
        print("human wins 1 point \n")
        print(f"computer_point is {computer_Points} and your point is {human_Points} \n ")
    elif n=="P" and ran=="S":
        human_Points=human_Points+1
        print(f"your guess {n} and computer guess is {ran} \n")
        print("human wins 1 point \n")
        print(f"computer_point is {computer_Points} and your point is {human_Points} \n ")
    elif n=="P" and ran=="C":
        computer_Points=computer_Points+1
        print(f"your guess {n} and computer guess is {ran} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_Points} and your point is {human_Points} \n ")
    elif n=="C" and ran=="S":
        computer_Points=computer_Points+1
        print(f"your guess {n} and computer guess is {ran} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_Points} and your point is {human_Points} \n ")
    elif n=="C" and ran=="P":
        human_Points=human_Points+1
        print(f"your guess {n} and computer guess is {ran} \n")
        print("human wins 1 point \n")
        print(f"computer_point is {computer_Points} and your point is {human_Points} \n ")
    else:
        print("You input wrong input")
    no_of_chance=no_of_chance+1
    print(f"{chance - no_of_chance} is left out of {chance} \n")
print("Game Over")
if computer_Points == human_Points:
    print("Tie")

elif computer_Points > human_Points:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_Points} and computer point is {computer_Points}")