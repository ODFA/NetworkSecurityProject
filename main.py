import numpy
import random

#Initializing hyperparamaters
layerOneNodes = 5
layerTwoNodes = 5
layerThreeNodes = 1

#Creating a sigmoid function to keep neuron values between 0 and 1, and so you can find the derivative of a point
def sigmoid(vector, derivativeMode = False):
	if derivativeMode: return (vector * (1 - vector)) #Return the derivative if in derivative mode
	else: return (1 / (1 + numpy.exp(-vector))) #Return sigmoid(x) if not in derivative mode

def getLabel(values):
	if (values[0] == 1 and values[-1] == 1): return 1 #If the first and last values of values is 1, return True
	else: return 0

#Creating random values for training data
trainingValues = numpy.array([[random.getrandbits(1) for i in xrange(layerOneNodes)] for j in xrange(pow(2, layerOneNodes))]) #Creating
idealOutputs = numpy.array([[getLabel(sample) for sample in trainingValues]]).T

#Creating random synapses
numpy.random.seed(1)
LayerOneSynapses = (numpy.random.random((layerOneNodes, layerTwoNodes)) * 2) - 1 #Create an array with layerOneNodes elements that contain arrays with layerTwoNodes elements that contain a value between -1 and 1
LayerTwoSynapses = (numpy.random.random((layerTwoNodes, layerThreeNodes)) * 2) - 1 #Create an array with layerTwoNodes elements that contain arrays with layerThreeNodes elements that contain a value between -1 and 1

#Training loop
for p in xrange(int(raw_input("Training iterations: "))):

	#Foward propegation
	inputValues = trainingValues
	hiddenValues = sigmoid(numpy.dot(inputValues, LayerOneSynapses)) #Find the dot product of inputValues and LayerOneSynapses, and put the list through the sigmoid function to keep Node values between 0 and 1
	outputValues = sigmoid(numpy.dot(hiddenValues, LayerTwoSynapses)) #Find the dot product of outputValues and LayerTwoSynapses, and put the list through the sigmoid function to keep the values between 0 and 1

	#Back propegation
	outputError = idealOutputs - outputValues
	outputDelta = outputError * sigmoid(outputValues, derivativeMode = True)
	hiddenError = numpy.dot(outputDelta, LayerTwoSynapses.T)
	hiddenDelta = hiddenError * sigmoid(hiddenValues, derivativeMode = True)

	LayerOneSynapses += numpy.dot(inputValues.T, hiddenDelta)
	LayerTwoSynapses += numpy.dot(hiddenValues.T, outputDelta)

while (True):

	inputValues = numpy.array([int(raw_input("0 or 1\n")) for r in xrange(layerOneNodes)])
	hiddenValues = sigmoid(numpy.dot(inputValues, LayerOneSynapses))
	outputValues = sigmoid(numpy.dot(hiddenValues, LayerTwoSynapses))

	print(outputValues) #TEMP
	print("Network Predicts: " + str(int(round(outputValues))))
