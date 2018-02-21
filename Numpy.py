"""
16 / Feb / 2018

author: Alejandro Guevara
"""

import numpy as np

list_nbrs = [1, 2, 3, 4, 5, 6]

# Numpy arrays
print('\nArrays creation')

nbrs = np.array([1, 2, 3, 4, 5, 6])
nbrs = np.array(list_nbrs)
print(nbrs)

print(np.zeros((5, 3))) # Creates a numpy array filled with zeros, with the shape (5, 3)

print(np.ones((3, 6)))  # Creates a numpy array filled with ones, with the shape (3, 6)

print(np.linspace(0, 100, 11))  # Create a numpy array, starting at 0, ending at 100, with
                                # 11 steps in between. So it has values equally distributed
                                # through the range 100-0. Said in other words, 11 numbers
                                # in between 0 and 100

print(np.arange(0, 10, dtype='uint8'))  # Pretty similar to range function, just that it returns
                                        # a numpy array instead of a python list. dtype can specify
                                        # the data type the resulting array will have

print(np.random.randint(0, 100, 11))    # Create a numpy array with random numbers, min 0
                                        # max 100, with shape (1, 11)

# Matrix Operations retrieved from: http://cs231n.github.io/python-numpy-tutorial/#numpy-datatypes

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

print('\nBasic matrix operation')

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))

print('\nVector and matrix product')

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))
