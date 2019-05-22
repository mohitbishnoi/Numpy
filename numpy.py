# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 10:22:15 2019

@author: Mohit
"""

# =============================================================================
# # Numpy = is a python package to perform all sort of algorithematic operation
# # such as sum,product,add or any calculations. it works only for numeric values
# # numpy  = numeric python
# =============================================================================

import numpy as np

# create a array with numpy function

array1 = np.array([10,20,30])

print(array1)

print(type(array1))

print(array1.dtype) # return data type of array value

array2 = np.array([10,20,30.5])
print(array2.dtype)

# array incluedes similar type of values only
# if one value is float, whole array is float

#Two dimensional array = we have to take nested list

array3=np.array([[10,20],[30,40],[50,60]])

print(array3)

print(array3.shape) # return diamension of array


# Extraction of data from array. it is same as list

array1[1]
array3[0][1]

# to extract 20,40,60 from array3

[array3[0][1],array3[1][1],array3[2][1]]


# create an aray with name price_array with below data
# [10,11,12,13
# 11,12,13,14
# 12,13,14,15
# 13,14,15,16]

# shape of array should be 4,4

array4=np.array([[10,11,12,13],[11,12,13,14],[12,13,14,15],[13,14,15,16]])
array4
print(array4.shape)

# Replace first 14, by 13,second 14 by 15,third 14 by 16

array4[1][3]=13
array4[2][2]=15
array4[3][1]=16
print(array4)

# create an numpy array with below given data
# 10,12,14.5,16,17,20
array5=np.array([10,12,14.5,16,17,20])
#1. find data type of given array
array5.dtype
#2. find number of values in given array
len(array5)
#3. find difference between first and third value
array5[0]-array5[2]
#4. find total of last 3 value
sum(array5[-3:])
array5[-3:].sum()
#5. find avarage of first 3 value
array5[0:2].mean()
#6. replce 17 with 18
array5[-2]=18
array5


# performing some operation on numpy array

#1 transfroming array
print(np.transpose(array3))

# Sorting data
print(-np.sort(-array4)) # decending order
print(np.sort(array4)) # ascending order

#3. genrating random values
print(np.random.randn(5)) # return 5 random values
print(np.random.randint(5,10,20)) # return 20 random integer value between 5 to 10
print(np.random.normal(0,1,10)) # return 10 random normalized values with mean 0 and std 1

# Combining two array

a = np.array([10,11,12])

np.add(a,10)

np.add(a,20)
np.add(a,30)

newarray = np.concatenate((a,np.add(a,10)))
print(newarray)
#--------------------------------------------------------------------------------
#np.arange() it will genarate sequential value
array5 = np.array([[10,11,12],[13,14,15],[16,17,18]])
array6 = np.array(np.arange(10,19).reshape(3,3))
# Find each row total
np.sum(array5,axis=1)

# find each coloumn total
np.sum(array5,axis=0)

# Find total of array
np.sum(array5)

# np.sum() it is used to sum the array values
# if we use axis=1, it will return row total
# if we use axis = 0, it will return column total


np.add(array5,2)
# this will add 2 to each value of array

# for count condition
array5>15
(array5>14).sum()



















