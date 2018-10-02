import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from mpmath import *
import math

# this method draws the decision boundary assuming that classification works
# if h > 0.5 y = 1, and if h < 0.5 y = 0
def draw(coefficients, X):
	draw_y = (- coefficients[0] - coefficients[1] * X[:,1]) / coefficients[2]
	draw_x = X[:,1]
	plt.plot(draw_x, draw_y, c="r")

def main():
	learning_rate = 0.1

	# getting iris data and setting features and outputs
	iris_path = "data/iris.data_2.csv"
	iris_data = pd.read_csv(iris_path)
	iris_array = iris_data.values
	# Y is the output, in this case it is 1 or 2
	Y = iris_array[:,5]
	# X is the features array. For now there are only two types of features
	X = iris_array[:,1:3].tolist()
	for x in X:
		x.insert(0, 1.0)
	X = np.asarray(X)
	print X
	print X[:,1]
	print X[:,2]
	m = len(Y)

	# drawing dots relevantly
	for i in range(len(Y)):
		if Y[i] == 0:
			plt.plot(X[i][1], X[i][2], "ro")
		else:
			plt.plot(X[i][1], X[i][2], "bo")

	# we know that there are 3 features each
	coefficients = [0, 0, 0]
	# TODO 1000?
	for k in range(1000):
		# Most of the things are same with linear regression, only hypothesis will
		# be different.
		Hypothesis = []
		for X_current in X:
			dot_product = np.dot(coefficients, X_current)
			hypothesis = 1.0 / (1.0 + math.exp(-dot_product))
			Hypothesis.append(hypothesis)
		
		# part below is for calculating coefficients
		# exactly the same as linear regression
		for j in range(len(coefficients)):
			cost_gradient = (1.0/m) * sum(X[:,j] * (Hypothesis - Y))
			coefficients[j] = coefficients[j] - (learning_rate * cost_gradient)	

	print coefficients	
	draw(coefficients, X)

main()
plt.show()
