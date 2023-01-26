import numpy as np
import matplotlib.pyplot as plot

a = np.matrix('2 2 2 2 2 2; 2 2 2 2 2 2')
b = np.matrix('1 3; 1 4')
# plot.imshow(a, cmap='gray')
plot.imshow(b.reshape(2,2), cmap='gray')

plot.show()
