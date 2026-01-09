import numpy as np
#splitting arrays
print('splitting array_1 in 2 parts')
print(np.split(array_1 , 2 ))
#defining a new 2D array for vertical and horizontal splitting
array_2D = np.array([[1,2,3],
                     [4,5,6]])
print('2D array is : ')
print(array_2D)
#splitting array_2D vertically
print('splitting array_2 vertically')
print(np.vsplit(array_2D , 2))
#splitting array_2D horizontally
print('splitting array_2D horizontally')
print(np.hsplit(array_2D , 3))
