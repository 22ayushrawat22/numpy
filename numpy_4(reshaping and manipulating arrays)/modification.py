#modifications in the array
#adding an element at the particular index in the 1D array using(.insert())
import numpy as np 
print('inserting element in the array')
array = np.array([34,52,12,36])
print(np.insert(array , 1 , 100 , axis=None))

#adding an element in the 2D array #axis=0 means (row) #axis=1 means (column)
print('inserting element in the higher dimesion array')
array_1 = np.array([[23,43,52],
                    [34,95,72]])
print('adding elements in the row using axis=0')
print(np.insert(array_1 , 1 , [1,2,3] , axis=0))
print('adding elements in the column using axis=1')
print(np.insert(array_1 , 2 , [4,5] , axis=1))

print('inserting elements in the array at the end using append function .append()')
print(np.append(array , [1,2,3,4]))

print('concatinating arrays #axis=None(default) or axis=0(means concatinating horizontally)')
array_2 = np.array([5,6,7,8])
print(np.concat((array , array_2) ))

print('removing element from the 1D array')
print(np.delete(array , 2 , axis=None))

print('removing element from the higher dimension array')
print(np.delete(array_1 , 1 , axis=0))
print(np.delete(array_1 , 1 , axis=1))
