
import matplotlib.pyplot as mp
import numpy as np
import math

phiPercent = 2 / (3 + math.sqrt(5))


def uebung8(x):
	return (x+1/3)**2

def unimodal1_1(x):
	return (-0.2*(x**4))+((x**2)-x)

def unimodal3_3(x):
	return 1-math.exp(-x**2)


def printSomethingUseful(func, interval, minima):

	fig = mp.figure()
	ax = fig.add_subplot(1, 1, 1)

	x_values = np.linspace(interval[0], interval[1], 100)
	ax.plot(x_values , [func(x) for x in x_values])
	ax.plot(minima[0], minima[1], 'ro')
	ax.annotate(str(minima[0]),(minima[0], minima[1]))

	mp.show()


def goldenSectionFAP(func, interval):

	left = interval[0]
	right = interval[1]

	mly = 0.0
	mry = 0.0

	while (right - left) > 0.0001:
		a = (right - left) * phiPercent
		mlx = left + a
		mrx = right - a

		if mly == 0.0:
			mly = func(mlx)
		if mry == 0.0:
			mry = func(mrx)

		if mly < mry:
			right = mrx
			mry = mly
			mly = 0.0

		else:
			left = mlx
			mly = mry
			mry = 0.0

	printSomethingUseful(func, interval, (mrx - (0.5*(mrx-mlx)), mry - (0.5*(-mly))))

	return


if __name__ == "__main__":
	# Which function shall be used, which interval shall be checked?
	funcToUse = unimodal3_3
	position = (-3, 3)

	# Do it!
	goldenSectionFAP(funcToUse, position)
	# -------------------------------------------------------------- #



