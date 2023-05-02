import numpy as np
import random as rand

one = [23.23,15.3,16.43,14.24,57.2]
print(one)
a = np.array(one)
print(a)

x = np.arange(2,11).reshape(3,3)
print(x)

x = np.arange(12,38)
print(x)
x = x[::-1]
print(x)

x = np.ones((3,3))
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)

one = np.array([0,10,20,40,60])
two = [0,40]
print(one)
print(two)
print(np.in1d(one,two))
print(np.intersect1d(one,two))
print(np.setdiff1d(one,two))

x = np.eye(6)
print(x)

arra1 = np.random.randint(0,5,(12,12))
print(arra1)
n = 4
i = 1 + (arra1.shape[0]-4)
j = 1 + (arra1.shape[1]-4)
result = np.lib.stride_tricks.as_strided(arra1, shape=(i, j, n, n), strides = arra1.strides + arra1.strides)
print(result)

rand_num = np.random.randint(low=1, high=24, size= 5)
print(rand_num)

rand_num2 = np.random.choice(10, 2)
print(rand_num2)

rand_num3 = rand.sample(range(1,24),5)
print(rand_num3)

x = np.random.normal(size=5)
print(x)

x = np.random.random((5,5))
print(x) 
xmin, xmax = x.min(), x.max()
print(xmin, xmax)

a= np.random.random((10,2))
x,y = np.atleast_2d(a[:,0], a[:,1])
d = np.sqrt( (x-x.T)**2 + (y-y.T)**2)
print(d)