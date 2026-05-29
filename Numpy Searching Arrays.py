#Where()Method - It will return only indexes

import numpy as np

a = np.array([1,4,2,3,4,5,4,6])
x = np.where(a==4)
print(x)

#Find indexes are which values are odd
b = np.array([10,34,18,90,43])
y = np.where(b%2==1)
print(y)

#Find greater than 40 numbers
c = np.array([4,17,50,87,41])
z = np.where(c>40)
print(z)

#SearchSorted()- Find index postion where value should be inserted in sorted array

a = np.array([10,20,30,40])
x = np.searchsorted(a,[7,18])
print(x)

#Search right side
b = np.array([6,7,8,9])
x = np.searchsorted(b,7,side="right")
print(x)

#Search left side
c = np.array([6,7,8,9])
x = np.searchsorted(c,7,side="left")
print(x)
d = np.searchsorted(c,[7,4,6])
print(d)

a = np.array([1,4,0,2,6])
print(np.sort(a))

b = np.array(['mango','apple','cherry'])
print(np.sort(b))

c = np.array([[3,2,4],[5,0,1]])
print(np.sort(c))

d = np.array([True,False,True])
print(np.sort(d))

#Filtering

#Getting some elemtns out of an existing array & creating a new array
#In np, you filter an array using a boolean index list
#Boolean Condtions 