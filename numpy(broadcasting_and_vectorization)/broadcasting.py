import numpy as np 
 
#giving 10% off on the price of every product
print('applying 10% off on the price of every product in the array at once using broadcasting method')
price = np.array([100,200,300])
discount = 10
final_price = price - (price * 0.1)
print(final_price)

#vectorization 
array_1 = np.array([1,2,3])
array_2 = np.array([6,7,8])
result_1 = array_1 + array_2
result_2 = array_2 * 3
print(result_1)
print(result_2)


