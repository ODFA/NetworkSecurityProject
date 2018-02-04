import numpy
import random
#Setting the amount of nodes in each layer
inputNodes = 100 #Place holder
hiddenNodes = 50
outputNodes = 10
#Setting how many training examples the network should go through
trainingIterations = int(input("How many training iterations?"))
#Creating a sigmoid function to keep neuron values between 0 and 1, and so you can find the derivative of a poing
def sigmoid(vector, derivativeMode = False):
	if derivativeMode: return (x * (x - 1)) #TODO Ask Elgin how this finds the derivative
	#Return a number to keep the neuron values between 0 and 1
	else: return (1 / (1 + numpy.exp(-x))
#TODO talk to Elgin about training data for digits
#Creating weights
#Will go unused for now, so I can allow myself to start with a simpler network
inputWeights = [random.uniform(-1, 1) for m in xrange(inputNodes)]
hiddenWeights = [random.uniform(-1, 1) for n in xrange(hiddenNodes)]
outputWeights = [random.uniform(-1, 1) for o in xrange(outputNodes)]
#Creating the synapses
#I will use my own for loop system for now, so I can understand it better
inputSynapses = np.array([[random.uniform(-1, 1) for i in xrange(hiddenNodes)] for j in xrange(inputNodes)]) #Is np.array needed?
hiddenSynapses = np.array([[random.uniform(-1, 1) for k in xrange(outputNodes)] for l in xrange(hiddenNodes)]) #"
#Training loop WIP
for p in xrange(trainingIterations):
	inputValues = null #Place holder
	hiddenValues = null
	OutputVales = null
	#TODO Back propogation

while (True):
	inputValues = null #Place holder
	outputValues =
	for q in outputValues:
		largest = 0
		if (q > largest):
			largest = q
	print(outputValues.index(largest))
