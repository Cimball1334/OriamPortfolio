import numpy as np
import matplotlib.pyplot as plot

# x = np.random.randint(5, size=10)
x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.random.randint(5, size=10)
# b = np.matrix('1 3; 1 4')
# plot.imshow(a.reshape(4,4), cmap='gray')
# plot.imshow(b.reshape(2,2), cmap='gray')
plot.plot(x,y)
plot.xlabel('X Axis')
plot.ylabel('Y Axis')
plot.title('A Random Int Line Graph')
plot.show()