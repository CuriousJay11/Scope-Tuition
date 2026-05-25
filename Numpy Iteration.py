import numpy as np

a = np.array([1,2,3])
for x in a:
    print(x)

b = np.array([[1,2,3],[4,5,6]])
for x in b:
    for y in x:
      print(y)

#First loop - Access the rows
#Second Loop - Acceses elements inside the rows
#Output
#1,2,3,4,5,6 under each other

c = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in c:
   for y in x:
      for z in y:
         print(z)

#Nditer()
#Syntax - nditer(array)

d = np.array([[1,2,3],[4,5,6]])
for x in np.nditer(d):
   print(x)

e = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in np.nditer(e):
   print(x)

#Ndenumerate() - To iterate through an array along with the index postions
# It gives index postion and the value at that postition
#Syntax - Ndenumerate(array)

f = np.array([1,2,3,4,5,6])
for idx, x in np.ndenumerate(f):
   print(idx,x)

g = np.array([[7,8,9],[10,11,12]])
for index, x in np.ndenumerate(g):
   print(index,x)

h = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for index, x in np.ndenumerate(h):
   print(index,x)