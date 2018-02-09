import numpy
import random
#Setting the number of nodes for each layer
inputNodes = 5
hiddenNodes = 5
outputNodes = 2
#Creating a sigmoid function to keep neuron values between 0 and 1, and so you can find the derivative of a point
def sigmoid(vector, derivativeMode = False):
	if derivativeMode: return (x * (x - 1)) #Return the derivative if in derivative mode
	else: return (1 / (1 + numpy.exp(-x)) #Return sigmoid(x) if not in derivative mode
#Creating the synapses
inputSynapses = np.random.random((inputNodes, hiddenNodes)) * 2 - 1 #Create an array with inputNodes elements that contain arrays with hiddenNodes elements that contain a value between -1 and 1
hiddenSynapses = np.random.random((hiddenNodes, outputNodes)) * 2 - 1 #Create an array with hiddenNodes elements that contain arrays with outputNodes elements that contain a value between -1 and 1
#Training loop
for p in xrange(int(raw_input("How many training iterations?"))):
	#Foward propegation
	inputValues = [random.randint(0, 2) for i in xrange(0, 6)] #Create a random data sample
	hiddenValues = sigmoid(numpy.dot(inputValues, inputSynapses)) #Find the dot product of inputValues and inputSynapses, and put the list through the sigmoid function to keep Node values between 0 and 1
	outputValues = sigmoid(numpy.dot(hiddenValues, hiddenSynapses)) #Find the dot product of outputValues and hiddenSynapses, and put the list through the sigmoid function to keep the values between 0 and 1
while (True):
	inputValues = null #Place holder
	outputValues =
	for q in outputValues:
		largest = 0
		if (q > largest):
			largest = q
	print(outputValues.index(largest))
