import numpy as np 

#checking whether number is missing at particular index or not in the array
print('checking whether number is missing at particular index or not in the array')
print('true means the value is missing , false means the value is present')
array = np.array([34,26,np.nan,67,np.nan])
checking = np.isnan(array)
print(checking)

#replacing the missing value with a particular number
print('replacing the missing values with a particular number')
inserting = np.nan_to_num(array , nan=100)
print(inserting)

#checing whether the array consists an infinite value or not
print('checing whether the array consists an infinite value or not')
print('true means (yes) an infinite number , false means (no) not an infinite number')
array_1 = np.array([21,92,45,np.inf,62,-np.inf,58])
infinite_or_not = np.isinf(array_1)
print(infinite_or_not)

#replcaing the infinite number with a finite number
print('replcaing the infinite number with a finite number')
replace = np.nan_to_num(array_1 , posinf=100 , neginf=-100)
print(replace) 