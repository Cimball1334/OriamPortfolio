import numpy as np


class NeuralNetwork:

    def __init__(self, layer_sizes):
        #creates a tuple where a is the number of columns and b is the number of rows
        #this comes from creating a matrix of our connections between neurons
        weight_shapes = [(a,b) for a,b in zip(layer_sizes[1:],layer_sizes[:-1])]
        
        #Stores the actual weight values for our weight shapes
        #()/s[1]**.5 normalizes all the values by dividing by the sqrt of the number of inputs to that layer s[1] so that values do not scale by size of the array             
        #sqrt info came from: https://cs231n.github.io/neural-networks-2/#init
        self.weights = [np.random.standard_normal(s)/s[1]**.5 for s in weight_shapes]
        #Stores the biases for each neuron connection
        self.biases = [np.zeros((s,1)) for s in layer_sizes[1:]]
        
        # print(weight_shapes)
        # print(self.weights)
        # print(self.biases)

    def predict(self, a):
        #this loop represents each layer where w is a specific layers weight and b is the bias
        for w,b in zip(self.weights,self.biases):
            # i  = np.matmul(w,a)+b
            # print(i[0])
            
            #matrix multiplication between the weights, and the previous neurons output, plus the bias for each neuron
            #a = output of this layer: activation function passing in the weight, previous layer, and adding bias as defined above
            a = self.activation(np.matmul(w,a) + b)
        #this is the output layer
        return a

    #determines how accurate our weights nad biases were in determining the proper output
    def print_accuracy(self,images,labels):
        predictions = self.predict(images)
        #total number correct by checking the sum of every time the max number in our prediction matched the max number of our expected output
        num_correct = sum([np.argmax(a) == np.argmax(b) for a,b in zip(predictions,labels)])
        #print statement that dispays part/whole of correct and its percentage
        print('{}/{} accuracy: {}%'.format(num_correct,len(images),(num_correct/len(images))*100))

    @staticmethod
    #sigmoid activation method is f(x) = 1/1+(e^-x) 
    #activation method is required for non linear function
    #if you plot the data of a binary question, there are regions where it is either yes or no, 
    #this is easy to imagine in 2d space as it can be represented on a graph, the more possible outcomes the more dimensions you have
    def activation(x):
        return 1/(1+np.exp(-x))
    
