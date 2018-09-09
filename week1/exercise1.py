import numpy as np

# Basics

# Create two arrays, a and b which each have the integers 0, 1, 2 ..., 1e7 - 1. 
# Use the normal arrays or lists of your programming language, e.g list or [] in Python.
a = []
b = []
for i in range(1,10000000):
    a.append(i)
    b.append(i)

# Create a function that uses a for-loop or equivalent to return a new array, 
# which contains the element-wise sum of a and b.
def add_with_for(a, b):
  c = []
  for i in range(0, len(a)):
    c.append(a[i]+b[i])      
  return c

# Now create another function that uses NumPy (or equivalent) to do the same. 
# To try it out, allocate two arrays (e.g np.array in NumPy) and add the arrays 
# together using your function. Don’t use loops, instead, find out how to add the 
# two arrays together directly. 
def add_with_numpy(a, b):
  c = np.add(a, b)
  return c

# c = add_with_for(a, b)

# c = add_with_numpy(a, b)


# Array manipulation

# Create desired arrays A, B, C and D
array = np.arange(100)
A = array.reshape(10, 10)
B = A % 2
C = np.ones((10, 10))
np.fill_diagonal(C, 0)
D = np.flip(C, 1)

# Call the last two matrices C and D, respectively. 
# Show that the determinant of their product (matrix multiplication) 
# is the same as the product of their determinants. 
# That is, calculate both det(CD) and det(C) * det(D), and show that they are the same. 
# Why does this hold in this instance? Does it hold in general?
det1 = np.linalg.det(np.matmul(C, D))
det2 = np.linalg.det(C)*np.linalg.det(D)
print("Determinant of product of C and D is", det1)
print("Product of determinants of C and D is", det2)


# Array Slicing

from sklearn.datasets import load_boston

# Load the Boston housing dataset. The data should be a matrix of shape (506, 13), 
# that is, it has 506 rows and 13 columns. Use the shape attribute of numpy arrays to verify this. 
boston = load_boston()
print(boston.data.shape)

# Select rows where the Crime feature (CRIM) is higher than 1. 
# The first few row numbers should be 16, 20, 22 (zero-indexed). How many are there?
crim = boston.data[:,0]
selected = np.where(crim > 1)
print(selected)
print('There are', len(selected[0]), 'rows.')

# Select the rows where the pupil-to-teach ratio is between 16% and 18% (exclusive). 
# There should be 100 of these.
ratios = boston.data[:,10]
selected = np.where(np.logical_and(ratios>16, ratios<18))
print(selected)
print('There are', len(selected[0]), 'rows.')

# Find the mean nitric oxides concentration for homes whose median price is 
# more than $25000 (the target variable). It should be around 0.492.
nitric = boston.data[:,4]
combined = np.vstack((nitric, boston.target)).T
selected = np.where(combined[:,1] > 25)
new = []
for x in selected[0]:
  new.append(nitric[x])
mean = np.mean(new)
print('The mean is', mean)