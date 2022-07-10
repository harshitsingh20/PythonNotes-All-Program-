# Using While loop
"""
n = 18
number_of_guesses = 1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses <= 9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number < 18:
        print("you enter less number please input greater number.\n")
    elif guess_number > 18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses, "no.of guesses he took to finish.")
        break
    print(9 - number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses > 9):
    print("Game Over")

"""

# Using For loop

h=55
for i in range(1, 10):
    n=int(input("Enter the Number: "))
    if i<9 or n==55:
        if n>h:
            print("You Input the Highest number")
            print("Number of Gusses remaning",9-i)
        elif n<h:
            print("You input the lowest number ")
            print("Number of Gusses remaning", 9 - i)
        else:
            print("You win")
            print("Number of Gusses remaning",i)
            break
    if (i==9):
        print("Game over")