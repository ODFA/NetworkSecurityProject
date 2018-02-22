import numpy
import random
#Setting the number of nodes for each layer
inputNodes = 5
hiddenNodes = 5
outputNodes = 1
trainingItterations = 10000
#Creating a sigmoid function to keep neuron values between 0 and 1, and so you can find the derivative of a point
def sigmoid(vector, derivativeMode = False):
	if derivativeMode: return (vector * (vector - 1)) #Return the derivative if in derivative mode
	else: return (1 / (1 + numpy.exp(-vector))) #Return sigmoid(x) if not in derivative mode
def ideal(values):
	if (values[0] == 1 and values[-1] == 1): return True
	else: return False
#Creating random values for training data
trainingValues = numpy.array([[random.getrandbits(1) for i in xrange(inputNodes)] for j in xrange(pow(2, inputNodes))])
idealOutputs = numpy.array([[ideal(sample) for sample in trainingValues]]).T
#Creating random synapses
numpy.random.seed(1)
inputSynapses = numpy.random.random((inputNodes, hiddenNodes)) * 2 - 1 #Create an array with inputNodes elements that contain arrays with hiddenNodes elements that contain a value between -1 and 1
hiddenSynapses = numpy.random.random((hiddenNodes, outputNodes)) * 2 - 1 #Create an array with hiddenNodes elements that contain arrays with outputNodes elements that contain a value between -1 and 1
#Training loop
print(hiddenSynapses)
for p in range(trainingItterations):
	#Foward propegation
	inputValues = trainingValues
	hiddenValues = sigmoid(numpy.dot(inputValues, inputSynapses)) #Find the dot product of inputValues and inputSynapses, and put the list through the sigmoid function to keep Node values between 0 and 1
	outputValues = sigmoid(numpy.dot(hiddenValues, hiddenSynapses)) #Find the dot product of outputValues and hiddenSynapses, and put the list through the sigmoid function to keep the values between 0 and 1
	#Back propegation
	outputError = idealOutputs - outputValues
	outputDelta = outputError * sigmoid(outputValues, derivativeMode = True)
	hiddenError = numpy.dot(outputDelta, hiddenSynapses.T)
	hiddenDelta = hiddenError * sigmoid(hiddenValues, derivativeMode = True)
	inputSynapses += numpy.dot(inputValues.T, hiddenDelta)
	hiddenSynapses += numpy.dot(hiddenValues.T, outputDelta)
print(hiddenSynapses)
while (True):
	inputValues = numpy.array([int(raw_input("0 or 1\n")) for r in xrange(0, 5)])
	hiddenValues = sigmoid(numpy.dot(inputValues, inputSynapses))
	outputValues = sigmoid(numpy.dot(hiddenValues, hiddenSynapses))
	print(outputValues)
	print("Network Predicts: " + str(int(round(outputValues))))
