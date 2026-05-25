#Numpy - Numerical Python
#Used to do scientific working or some scienctific computing with numerical data
#Matrix - Rows and Columns
#Pandas
#Matplotlib
#Scipy
#Data analysis, Ml, Image preocessing, Scientific Simulation

#import numpy:

import  numpy as np #Syntax

#Create array

a = np.array([1,2,3,4])
print (a)

#Python List  |  Numpy Array
#Slower       |  Faster
#More memory  |  Less Memory
#Cannot perform    Supports Vector Operations
#Vector Operations

#Types of array
#1d array
# 2D array 

b = np.array([[1,2],[3,4]])
print(b)

# 3D Array

c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)

#Two blocks output

#How to check dimension

print(c.ndim)  # Check dimensions
print(c.shape) #Rows and columns
print(c.size)  # Total elements
print(c.dtype) #Check data type

#*In numpy every array has a datatype
# int64 --> 64 bits of memory
#   |
# integer

#Float64

d = np.array([1.7,3.4])
print(d.dtype)
e = np.array([True,False,True])
print(e.dtype)

#Shape attributes will tell you structure of
#array, no of rows, no of columns, no of layers
a = np.array([1,2,3,4])
print(a.shape)

#no of elements in 1 row
#2d arary
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)

c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)
print(c.shape)


a = np.array([1,2,3,4])
print(a[0])
print(a[2]+a[3])
print(a[1:])

b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(b)
print(b[0,1])
print(b[1,4])

c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c[0,1,1])
print(c[1,1,0])

d = np.array([[1,2],[3,4]])
print(d)
print(d[1,1])

e = np.array([1,2,3,4,5,6])
print(e[1:4])
print(e[:3])
print(e[::2])

#Chaning the datatype using dtype
b = np.array([1,2,3],dtype = "float32")
print(b)
print(b.dtype)

flt = np.array([1.2,4.6,6.8,8.4])
print(flt)
print(flt.dtype)

cox = np.array([2+3j,5+3j])
print(cox)
print(cox.dtype)

bool = np.array([True,False,False])
print(bool)
print(bool.dtype)

flt = np.array([1.2,4.6,6.8,8.4],dtype = "int32")
print(flt)
print(flt.dtype)


#Numpy convert everything to float automatically
z = np.array([1,4.6,3])
print(z)
print(z.dtype)

s = np.array([12,234,4960],dtype = "S")
print(s)
print(s.dtype)

arr = np.array([1,2,3,4,0,-2])
newarr = arr.astype('bool')
print(newarr)

#Copy vs View
#Copy -  New array
#View - Original Array

#Copy
a = np.array([1,2,3,4,5])
x = a.copy()
a[0] = 42
print(a)
print(x)

#View
a = np.array([1,2,3,4,5])
x = a.view()
a[0] = 42
print(a)
print(x)

#How to reshape dimesions 1d to 2d
#No of elements in each dimension
#Convert 10 with 12 element into 2d array

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a)
b = a.reshape(3,4)
print(b)

#1d to 3d
c = a.reshape(2,2,3)
print(c)

#(2,2,2)

#Blocks,Rows,Columns

z = np.array([1,2,3,4,5,6,7,8])
e = z.reshape (2,2,-1)
print(e)
print(a.reshape(2,-1))


arr = np.array([[1,2,3],[4,5,6]])
newarr = arr.reshape(6)
print(newarr)


#Flatten() to convert any array to 1d
#Ravel( to convert any array to 1d)
#Transpose() - Convert rows to columns

a = np.array([[1,2],[3,4]])
print(a.flatten())
       #OR 

a = np.array([[1,2],[3,4]])
print(a.ravel())

a = np.array([[1,2,3],[4,5,6]])
print(a.T)