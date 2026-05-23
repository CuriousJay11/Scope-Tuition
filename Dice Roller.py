import random 

print("Dice Roller\n")
Choice = (input("Roll: Yes or No:  "))

if Choice == "Yes":
  Roll = random.randint(1, 6)
  print("You got a lucky!",Roll)

else:
  print("Ok, come back later!")





