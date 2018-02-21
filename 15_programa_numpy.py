# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 17:41:11 2018

@author: JC
"""

import numpy as np

lista = [[1, 2, 3],[ 4, 5, 6]]

# Numpy arrays
print('\nArrays creation')
nbrs = np.array([1, 2, 3, 4, 5, 6])
nbrs = np.array(lista)
print(nbrs)
print('\n\nArrays indexing')
print(nbrs[:,:2])

print('\n\nArray zeros')
print(np.zeros((5, 3))) # Creates a numpy array filled with zeros, with the shape (5, 3)
                        # rowsxcolumns
print('\n\nArray ones')
print(np.ones((3, 6)))  # Creates a numpy array filled with ones, with the shape (3, 6)

print('\n\nArray linspace')
print(np.linspace(0, 100, 11))  # Create a numpy array, starting at 0, ending at 100, with
                                # 11 steps in between. So it has values equally distributed
                                # through the range 100-0. Said in other words, 11 numbers
                                # in between 0 and 100

print('\n\nArray range')
print(np.arange(0, 10, dtype='uint8'))  # Pretty similar to range function, just that it returns
                                        # a numpy array instead of a python list. dtype can specify
                                        # the data type the resulting array will have

print('\n\nArrays random')
print(np.random.randint(0, 100, 11))    # Create a numpy array with random numbers, min 0
                                        # max 100, with shape (1, 11)

# Matrix Operations

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

print('\n\nBasic matrix operation')
# Elementwise sum
print(x + y)
print(np.add(x, y))

# Elementwise difference
print(x - y)
print(np.subtract(x, y))

# Elementwise product
print(x * y)
print(np.multiply(x, y))

# Elementwise division
print(x / y)
print(np.divide(x, y))

# Elementwise square root
print(np.sqrt(x))

print('\n\nVector and matrix product')
# Inner product of vectors
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product
print(x.dot(y))
print(np.dot(x, y))

print('\n\nArrays extra operations')
#print(nbrs[3:5])
lista_2 = [1,2,0,0,4,0]
a = np.array(lista_2)
print(np.nonzero(a)) # Indices of the non-zero elements in an array
print(a)
print(a.shape) # Dimmensions of the array
print(a.T)
a = np.atleast_2d(lista_2)
print(a) # Creates an array with at least two dimenssions
print(a.shape)
print(a.T)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(np.concatenate((a, b), axis=0)) # Concatenation of two arrays along a defined dimmension

a = np.arange(12).reshape(3, 4)
print(a)
print(a.shape)
print(a.T)
