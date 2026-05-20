import random


print("Winning Rules:")
print("Paper beats Rock")
print("Rock beats Scissor")
print("Scissor beats Paper")
print("Same choices lead to tie\n")

choice = int(input("Enter a choice - 1.Rock, 2.Paper, 3.Scissor: "))

# Match player choice
if choice == 1:
    print("You chose Rock")
elif choice == 2:
    print("You chose Paper")
elif choice == 3:
    print("You chose Scissors")
else:
    print("Invalid choice!")

computer_choice = random.randint(1, 3)

if computer_choice == 1:
    print("Computer chose Rock")
elif computer_choice == 2:
    print("Computer chose Paper")
else:
    print("Computer chose Scissors")

if choice == computer_choice:
    print("Its a tie")

elif choice == 2:
    print

if choice == computer_choice:
    print("It's a tie")
elif (choice == 1 and computer_choice == 3) or (choice == 2 and computer_choice == 1) or (choice == 3 and computer_choice == 2):
    print("You win!")
else:
    print("Computer wins!")

again = (input("Do You want to play again(Y/N)"))

if again == "Y":
    print("")
else:
    print("Thanks for playing")





