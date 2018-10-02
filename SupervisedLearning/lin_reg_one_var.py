import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from mpmath import *

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

	m_current, b_current = 0, 0
	for i in range(1000):
		y_current = (m_current * X) + b_current
		cost = sum([data**2 for data in (Y-y_current)]) / (2*m)
		m_gradient = -(1/m) * sum(X * (Y - y_current))
		b_gradient = -(1/m) * sum(Y - y_current)
		m_current = m_current - (learning_rate * m_gradient)
		b_current = b_current - (learning_rate * b_gradient)

	coefficients = [m_current, b_current]

	hypothesis = np.poly1d(coefficients)
	print coefficients
	print hypothesis
	plt.plot(X, Y, "o")
	plt.plot(X, hypothesis(X), c="g")
	
main()
plt.show()
