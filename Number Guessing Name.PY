
import random

low = int(input("Enter lowest number in range: "))
high = int(input("Enter highest number in range: "))
num = random.randint(low, high)

guess = None  

while guess != num:
    guess = int(input("Enter your guess within the range: "))
    
    if guess == num:
        print("Congratulations, You got it right!")
    elif guess > num:
        print("The number is lower")
    elif guess < num:
        print("The number is higher")
    else:
        print("Congratulation your answer is Invalid, Try guessing another number")


        

