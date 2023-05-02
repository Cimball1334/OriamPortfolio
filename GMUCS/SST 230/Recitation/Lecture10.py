import numpy as np

x = np.arange(6)
print("\nOriginal array:")
print(x)
r1 = np.mean(x)
r2 = np.average(x)
assert np.allclose(r1, r2)
print("\nMean: ", r1)
r1 = np.std(x)
r2 = np.sqrt(np.mean((x - np.mean(x)) ** 2 ))
assert np.allclose(r1, r2)
print("\nstd: ", 1)
r1= np.var(x)
r2 = np.mean((x - np.mean(x)) ** 2 )
assert np.allclose(r1, r2)
print("\nvariance: ", r1)

# 

x = np.array([0, 1, 3])
y = np.array([2, 4, 5])
print("\nOriginal array1:")
print(x)
print("\nOriginal array1:")
print(y)
print("\nPearson product-moment correlation coefficients of the said arrays:\n",np.corrcoef(x, y))

# 

a = np.arange(9).reshape((3,3))
print("Original flattened array:")
print(a)
print("Weighted average along the specified axis of the above flattened array:")
print(np.average(a, axis=1, weights=[1./4, 2./4, 2./4]))

# 

array1 = [0, 1, 6, 1, 4, 1, 2, 2, 7] 
print("Original array:")
print(array1)
print("Number of occurrences of each value in array: ")
print(np.bincount(array1))

# 

x = np.round([1.45, 1.50, 1.55])
print(x)
x = np.round([0.28, .50, .64], decimals=1)
print(x)
x = np.round([.5, 1.5, 2.5, 3.5, 4.5]) # rounds to nearest even value
print(x)

# 

x = np.random.random((5,3))
print("First array:")
print(x)
y = np.random.random((3,2))
print("Second array:")
print(y)
z = np.dot(x, y)
print("Dot product of two arrays:")
print(z)

# 

print("Roots of the first polynomial:")
print(np.roots([1, -4, 7]))
print("Roots of the second polynomial:")
print(np.roots([1, -11, 9, 11, -10]))

# 

print("sine: array of angles given in degrees")
print(np.sin(np.array((0., 30., 45., 60., 90.)) * np.pi / 180.))
print("cosine: array of angles given in degrees")
print(np.cos(np.array((0., 30., 45., 60., 90.)) * np.pi / 180.))
print("tangent: array of angles given in degrees")
print(np.tan(np.array((0., 30., 45., 60., 90.)) * np.pi / 180.))

# 

x = np.array([1, 3, 5, 7, 0])
print("Original array: ")
print(x)
print("Difference between neighboring elements, element-wise of the said array.")
print(np.diff(x))

# 

from numpy import linalg as LA
a = np.array([[1, 0, -1], [0, 1, 0], [1, 0, 1]])
print("Original matrix:")
print(a)
print("The condition number of the said matrix:")
print(LA.cond(a))

# 

a = np.array([[1,2],[3,4]])
print("Original array:")
print(a)
result =  np.linalg.det(a)
print("Determinant of the said array:")
print(result)

# 

m = np.array([[1,2],[3,4]])
print("Original matrix:")
print(m)
result =  np.linalg.inv(m)
print("Inverse of the said matrix:")
print(result)

# 

m = np.arange(9).reshape(3,3)
print("Original matrix:")
print(m)
result =  np.trace(m)
print("Sum of the diagonal elements of the matrix is:")
print(result)

# 

x = np.arange(24).reshape((2,3,4))
print("Array x:")
print(x)
print("Array y:")
y = np.arange(4)
print(y)
print("Inner of x and y arrays:")
print(np.inner(x, y))

# 

m = np.mat("2 1;1 2")
print("Original matrix:")
print("a\n", m)
w, v = np.linalg.eig(m) 
print( "Eigenvalues of the said matrix",w)
print( "Eigenvectors of the said matrix",v)

# 







