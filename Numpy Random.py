import numpy as np
from numpy import random

#Generate random float
x = random.randint(100)
print(x)

#Generate random array
y = random.randint(100,size=5)  #1d
print(y)

arr = random.randint(100,size=(3,5))  #2d
print(arr)

#How to generate random number from array

#Choice() METHOD - Allow You To Generate A Random Value Based On An Array Of Value

a = random.choice([3,5,7,9])
print(a)

b = random.choice([3,5,7,9],size=(3,5))
print(b)

#Choice method takes an array as parameter & randomly returns one of the value

#Shuffle Array

arr = np.array([2,3,4,5,1])
random.shuffle(arr)
print(arr)

#Probability Distribution Function
#Probability of all values in an array
#Choice() #Specify the prob for each value

x = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(100))
print(x)

#Permutation

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(np.random.permutation(arr))

print(arr)

#Shuffle no 1-10
arr = np.array([1,2,3,4,5,6,7,8,9,10])
random.shuffle(arr)
print(arr)

#Random Arrangement of names
a = np.array(["Jilly",'Billy','Dilly','Silly','Killy'])
random.shuffle(a)
print(a)

#Shuffle studnet roll no
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
random.shuffle(arr)
print(arr)

#Shuffle Quiz Question
import numpy as np
from numpy import random


quiz_questions = np.array([
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is 5 + 7?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the chemical symbol for water?"
])

random.shuffle(quiz_questions)
print(quiz_questions)

#Random card numbers
x = random.randint(0,10,size=11)
print(x)



