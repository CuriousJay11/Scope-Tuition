import random 

print("Coin Toss\n")
Choice = (input("Roll: Yes or No:  "))

if Choice == "Yes":
  Flip = random.choice(["Heads", "Tails"])
  print("You got a lucky!",Flip)

else:
  print("Ok, come back later!")