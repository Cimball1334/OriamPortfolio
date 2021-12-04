import NeuralNetwork as nn
import numpy as np
import matplotlib.pyplot as plot

with np.load('C:\\Users\\kimba\\git\\CollegeClasses\\OriamPortfolio\\NeuralNetworks\\mnist.npz') as data:
    training_images = data['training_images']
    training_labels = data['training_labels']
    
'''visualization code:'''
# plot.imshow(training_images[0].reshape(28,28), cmap = 'gray')
# plot.show()

layer_sizes = (784,5,10)

'''simulated input'''
# x = np.ones((layer_sizes[0],1))

net = nn.NeuralNetwork(layer_sizes)
prediction = net.predict(training_images)

'''prints the dimension of the matrix'''
# print(prediction.shape)

#prints the highest prediciton - in this case also the number that it believes that it is
#print('Number is a {} with ({:.2f}%) confidence'.format( np.argmax(prediction[0]) , prediction[0][np.argmax(prediction[0])][0]*100))

net.print_accuracy(training_images,training_labels)