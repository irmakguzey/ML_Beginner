import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from mpmath import *

# this is the improved version of linear regression with one variable
# this one is easier to adjust ti multiple variables

def main():
	learning_rate = 0.01
	coefficients = [0, 0]
	
	# getting iris data
	iris_path = "data/iris.data.csv"
	iris_data = pd.read_csv(iris_path)
	iris_array = iris_data.values
	print iris_array
	X = iris_array[:,3] # input variables
	Y = iris_array[:,2] # outputs
	m = float(len(X))
	rand_index = random.sample(range(len(X)), 1)
	coefficients = [Y[rand_index[0]] / X[rand_index[0]],0]
	hypothesis = np.poly1d(coefficients)
	plt.plot(X, hypothesis(X), c="b")

	cost_array = [0]

	m_current, b_current = 0, 0
	while True:
		y_current = (coefficients[0] * X) + coefficients[1]
		cost = sum([data**2 for data in (Y-y_current)]) / (2*m)	
		cost_array.append(cost)
		coefficients[0] = coefficients[0] - (learning_rate * (-(1/m) * sum(X * (Y - y_current))))
		coefficients[1] = coefficients[1] - (learning_rate * (-(1/m) * sum(Y - y_current)))
		if abs(np.gradient(cost_array)[-1]) < 0.000001:
			break

	hypothesis = np.poly1d(coefficients)
	print coefficients
	print hypothesis
	plt.plot(X, Y, "o")
	plt.plot(X, hypothesis(X), c="g")
	
main()
plt.show()
