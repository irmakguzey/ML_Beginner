import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

def whereIsDot(x,y, rect): #this function will return 0 if the dot is inside the rect, 1 for top of rect, 2 -> right, 3 -> below, 4 -> left
	rect_x = rect.get_x()
	rect_y = rect.get_y()
	rect_width = rect.get_width()
	rect_height = rect.get_height()
	if x > rect_x:
		if x > (rect_x + rect_width): #means it is at right
			return 2
		else:
			if y > rect_y:
				if y > (rect_y + rect_height): #means it's at the top
					return 1
				else:
					return 0
			else:
				return 3 #it is below
	else:
		return 4 #it is at left


hab_path = "data/iris.data_2.csv"
hab_data = pd.read_csv(hab_path)
hab_array = hab_data.values
X = hab_array[:,1]
Y = hab_array[:,2]
classArr = hab_array[:,5]

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
blue_rect = patches.Rectangle((1,1), 1, 1, fill=False, color="b") #it will have the blue dots inside
red_rect = patches.Rectangle((5,1), 1, 1, fill=False, color="r")
blue_dots= [[],[]] #0th array is for x coordinates, 1th array is for y coordinates
red_dots = [[],[]]


for i in range(len(X)):
	if classArr[i] == 2:
		ax.plot(X[i], Y[i], "ro")
		red_dots[0].append(X[i])
		red_dots[1].append(Y[i])
	else:
		ax.plot(X[i], Y[i], "bo")
		blue_dots[0].append(X[i])
		blue_dots[1].append(Y[i])


rand_blue = random.choice(range(len(blue_dots)))
rand_red = random.choice(range(len(red_dots)))

blue_rect = blue_rect = patches.Rectangle((blue_dots[0][rand_blue],blue_dots[1][rand_blue]), 1, 1, fill=False, color="b")
red_rect = patches.Rectangle((red_dots[0][rand_red],red_dots[1][rand_red]), 1, 1, fill=False, color="r")


#for blue_rect:
for i in range(len(blue_dots[0])):
	dot_sit = whereIsDot(blue_dots[0][i], blue_dots[1][i], blue_rect)
	while dot_sit != 0:

		height = blue_rect.get_height()
		width = blue_rect.get_width()
		rect_x = blue_rect.get_x()
		rect_y = blue_rect.get_y()

		if dot_sit == 1:
			blue_rect.set_height(height + 0.1)
		elif dot_sit == 2:
			blue_rect.set_width(width + 0.1)
		elif dot_sit == 3:
			blue_rect.set_height(height + 0.1)
			blue_rect.set_y(rect_y - 0.1)
		else:
			blue_rect.set_width(width + 0.1)
			blue_rect.set_x(rect_x - 0.1)

		dot_sit = whereIsDot(blue_dots[0][i], blue_dots[1][i], blue_rect)

#for red_rect
for i in range(len(red_dots[0])):
	dot_sit = whereIsDot(red_dots[0][i], red_dots[1][i], red_rect)
	while dot_sit != 0:

		height = red_rect.get_height()
		width = red_rect.get_width()
		rect_x = red_rect.get_x()
		rect_y = red_rect.get_y()

		if dot_sit == 1:
			red_rect.set_height(height + 0.1)
		elif dot_sit == 2:
			red_rect.set_width(width + 0.1)
		elif dot_sit == 3:
			red_rect.set_height(height + 0.1)
			red_rect.set_y(rect_y - 0.1)
		else:
			red_rect.set_width(width + 0.1)
			red_rect.set_x(rect_x - 0.1)

		dot_sit = whereIsDot(red_dots[0][i], red_dots[1][i], red_rect)


ax.add_patch(blue_rect)
ax.add_patch(red_rect)
plt.ylim((-1,3))
plt.xlim((0,8))
plt.show()