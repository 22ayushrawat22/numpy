#array basic operations 

import numpy as np
array = np.array([[1,2,3,4],
                 [5,6,7,8]])
print(array+2)#addition
print(array-2)#subtraction
print(array*2)#multiplication
print(array/2)#division


print('aggregation functions in numpy')

print(np.sum(array))#sum of all the elements in the array
print(np.mean(array))#mean of the array
print(np.min(array))#minimum element in the array
print(np.max(array))#maximum element in the array
print(np.var(array))#variance of the array
print(np.std(array))#standard deviation of the array