#Start : End
#[1:5]
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[-3:-1])
print(arr[1:5:2])

#Start:Stop:Step

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a[1,1:4])
print(a[0,1:3])
print(a[0:2,2])