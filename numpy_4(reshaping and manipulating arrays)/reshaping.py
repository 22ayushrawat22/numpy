#reshaping arrays

import numpy as np

print('reshaping array from 1D to 2D')
array_1D = np.array([10,20,30,40,50,60])
print('one dimesion array is :')
print(array_1D)
array_2D= array_1D.reshape(2,3)
print('second dimension array is :')
print(array_2D)

print('reshaping array from 1D to higher dimensions(3D)')
array__1D = np.array([23,43,54,34,67,95,12,79,63])
print('one dimesion array is :')
print(array__1D)
array_3D = array__1D.reshape(3,3)
print('higher dimeasion array is : ')
print(array_3D)

#flattening arrays(changing the arrays from higher dimesions to 1D)
#we have two functions 
#1..ravel()(it gives us the view)
#2.flatten()(it gives us the copy)

array_HD = np.array([[23,43,12],
                     [45,28,94]])
print(array_HD.ravel())
print(array_HD.flatten())

