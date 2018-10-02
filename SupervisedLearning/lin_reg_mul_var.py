import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from mpmath import *

# this method returns the ratio of right guesses
# if the return value is close to 0, it is better
def train(coefficients, X, Y):
	# since the first element of X is one, dot product will give;
	# y = q0*x0 + q1*x1 + ...
	Y_test = []
	for x_current in X:
		y_test = np.dot(coefficients, x_current)
		Y_test.append(y_test)
	# print "Y_test: ", Y_test
	# print "Y: ", Y
	# print "Difference: ", abs(Y_test - Y)
	return sum((Y_test - Y) ** 2)

def main():
	learning_rate = 0.001
	
	# getting iris data and setting features and outputs
	iris_path = "data/iris.data.csv"
	iris_data = pd.read_csv(iris_path)
	iris_array = iris_data.values
	classes = iris_array[:,4]
	# since there are three classes we take one portion of classes
	m = len(classes) / 3
	X = iris_array[0:m][:,0:3].tolist()
	# to generalize functions 1 is added so that when multiplied, it will not
	# effect
	for x in X:
		x.insert(0,1)
	X = np.asarray(X)
	print X
	Y = iris_array[0:m][:,3]
	print Y
	m = float(m)
	print m

	# we know that there are 4 features
	# TODO also think of a way to generalize # of coefficients
	coefficients = [0,0,0,0]	
	cost_array = [0]
	Diffs = []
	for k in range(1000):
		Y_current = []
		for X_current in X:
			y_current = np.dot(coefficients, X_current)
			Y_current.append(y_current)
			#print 'y_current is: ', y_current, "size of Y_Current: ", len(Y_current)
		#print "size of Y: ", len(Y)
		cost = sum([data**2 for data in (Y-Y_current)]) / (2*m)
		cost_array.append(cost)
		for j in range(len(coefficients)):
			cost_gradient = -(1/m) * sum(X[:,j] * (Y - Y_current))
			coefficients[j] = coefficients[j] - (learning_rate * cost_gradient)
		# see the growth in training
		# print "train method's result is: ", train(coefficients, X, Y)
		Diffs.append(train(coefficients, X, Y))
		#if abs(np.gradient(cost_array)[-1]) < 0.00001:
		#	break
	
	ToPlot = []
	for j in range(len(Diffs)):
		ToPlot.append(j)

	plt.plot(ToPlot, Diffs, c="r")
	
main()
plt.show()
