import numpy as np

#stacking arrays #.vstack(it means stacking arrays vertically) 
#.hstack(it means stacking array horizontally)
array_1 = np.array([34,52,61,23])
print('first array is : ' , array_1)
array_2 = np.array([45,89,96,72])
print('second array is : ' , array_2)
print('stacking arrays vertically :' )
print( np.vstack((array_1 , array_2)))
print('stacking arrays horizontally :' )
print(np.hstack((array_1 , array_2)))

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
