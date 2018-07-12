import pandas as pd
import matplotlib.pyplot as plt
import random
from numpy import ones,vstack
from numpy.linalg import lstsq
import numpy as np
import math
import sys

def getLine(x,y): #x and y are arrays that represents two points
	
	points = [(x[0],y[0]),(x[1],y[1])]
	x_coords, y_coords = zip(*points)
	A = vstack([x_coords,ones(len(x_coords))]).T
	m, c = lstsq(A, y_coords)[0]
	line = "{m}x+y+{c}=0".format(m=-m, c=-c)
	print "Line Solution is ", line
	return line

def setSlopeandConst():
	global slope
	global constant
	for x in line:
		if x == "x":
			slope = float(line[0:(line.index(x))])
			#print slope
		elif x == "y":
			constant = float(line[(line.index(x)+2):(line.index("="))])
			#print constant

	
def getDistToLine(x,y): #x and y are points and this method calculates the distance of a certain point to the line 
	#print "x is: ", x , "y is: ", y
	setSlopeandConst()
	dist = abs(slope * x + y + constant) / ((slope**2 + 1) ** (1/2.0))
	#print "dist is : {dist}".format(dist=dist)
	return dist

def getDistToPoint(x,y,target_x,target_y):
	dist = ((target_x-x)**2 + (target_y-y)**2)**(1/2.0)
	return dist

def totalDist(): #total distance of all the chosen points to the line
	total_dist = 0.0
	for i in range(len(chosen_points[0])):
		total_dist += getDistToLine(chosen_points[0][i], chosen_points[1][i])
	return total_dist

def printCurrents():
	for i in range(len(chosen_points[0])):
		print "x is: ", chosen_points[0][i], "y is: ", chosen_points[1][i]

def printPoints(x,y):
	print "x is: ", x, "y is: ", y

line = "mx+y+c=0"
slope = 0
constant = 0

iris_path = "data/iris.data.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
iris_data = pd.read_csv(iris_path, names=names)
iris_array = iris_data.values
X = iris_array[:,3]
Y = iris_array[:,2]

plt.plot(X,Y,"o")

#sample X and Y keeps two random point at first, but then we will change the points in there and repeatedly call getLine method
rand_point = random.sample(range(len(X)), 2)
line_X = [X[rand_point[0]], X[rand_point[1]]]
line_Y = [Y[rand_point[0]], Y[rand_point[1]]]


chosen_points = [[line_X[0], line_X[1]], [line_Y[0], line_Y[1]]] #points that are travelled, it is two dimensional array every time a point is added chosen_points[0].append(new_x) and chosen_points[1].append(new_y) must be made

plt.plot(chosen_points[0], chosen_points[1], "go")
plt.plot(line_X, line_Y)
line = getLine(line_X, line_Y)

pastLines = [getLine(line_X, line_Y)]
totalDists = []

for i in range(len(X)): #it will stop when it minimizes the distance for all the points

	plt.plot(X[i], Y[i], "ro")

	#printCurrents()
	#printPoints(X[i], Y[i])


	if (not X[i] in chosen_points[0]) or (not Y[i] in chosen_points[1]):
		first_dist = getDistToPoint(X[i], Y[i], line_X[0], line_Y[0])
		second_dist = getDistToPoint(X[i], Y[i], line_X[1], line_Y[1])
		
		prev_dists = sys.maxint
		curr_dists = totalDist() + getDistToLine(X[i], Y[i])
		#print "calculated totalDist"
		prev_line = line #lines will change repeatedly as well
		curr_line = line
		while prev_dists > curr_dists: #should call getLine method repeatedly, changing the line
			prev_dists = curr_dists
			prev_line = curr_line

			if second_dist > first_dist: #first point will be changed according to the distance to the chosen point

				dummyX = line_X[0]
				dummyY = line_Y[0]

				if dummyX > X[i]:
					dummyX -= 0.05
				elif dummyX < X[i]:
					dummyX += 0.05

				if dummyY > Y[i]:
					dummyY -= 0.2
				elif dummyY < Y[i]:
					dummyY += 0.2

				line_X[0] = dummyX
				line_Y[0] = dummyY
			
			else:

				dummyX = line_X[1]
				dummyY = line_Y[1]

				if dummyX > X[i]:
					dummyX -= 0.05
				elif dummyX < X[i]:
					dummyX += 0.05

				if dummyY > Y[i]:
					dummyY -= 0.2
				elif dummyY < Y[i]:
					dummyY += 0.2

				line_X[1] = dummyX
				line_Y[1] = dummyY

			line = getLine(line_X, line_Y)	

			#plt.plot(line_X, line_Y)
			curr_dists = totalDist() + getDistToLine(X[i], Y[i])
			curr_line = line

		curr_dists = prev_dists
		curr_line = prev_line
		line = curr_line
		pastLines.append(curr_line)	
		setSlopeandConst()

	plt.plot(chosen_points[0], chosen_points[1], "go")
	chosen_points[0].append(X[i])
	chosen_points[1].append(Y[i])
	
	#print line
	#plt.plot(line_X, line_Y, c="r")
	pastLines.append(line)

setSlopeandConst()
#plt.plot(X, -slope*X -constant, c="b", linewidth="1.7")


#below lines are to find the line with the minimum distance in total
minDist = sys.maxint
minIndex = 0
for pastline in pastLines:

	line = pastline
	setSlopeandConst()
	totDist = totalDist()
	print pastline
	print totDist
	if minDist > totDist:
		minDist = totDist
		minIndex = pastLines.index(pastline)

line = pastLines[minIndex]
setSlopeandConst()
plt.plot(X, -slope*X -constant, c="g", linewidth="2.7")


plt.show()



