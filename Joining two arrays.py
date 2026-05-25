#Joining two arrays
#Combining two or more arrays into 1 array
#Concatenate()

import numpy as np


a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.concatenate((a,b))
print(c)

#Stack Function
#It will join arrays along a new axis

c = np.stack((a,b))
print(c)

#Vertical Stack
#Join arrays vertically , row wise
#Vstack

c = np.vstack((a,b))
print(c)

#same output as stack

#Hstack
#Join arrays horizontally, column wise
c = np.hstack((a,b))
print(c)

#Depth Stack

c = np.dstack((a,b))
print(c)

#Join array depth wise

d = np.array([1,2,3,4,5,6])
e = np.split(d,3)
print(e)
#Split into 3 equal array

d = np.array([1,2,3,4,5])
e = np.array_split(d,3)
print(e)

f = np.array([[1,2,3,4],[5,6,7,8]])
print(np.hsplit(f,2))

g = np.array([[1,2],
              [3,4],
              [5,6],
              [7,8]])

print(np.vsplit(g,2))