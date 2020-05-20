
import matplotlib.pyplot as mp
import numpy as np
import math

phiPercent = 2 / (3 + math.sqrt(5))

def FToAnalyze(x):
	return (x+1/3)**2


def printSomething():
	fig = mp.figure()
	ax = fig.add_subplot(1,1,1)

	x_values = list(range(-10,10))
	ax.plot (x_values, [FToAnalyze(i) for i in x_values], x_values, [(-FToAnalyze(i)) for i in x_values])
	ax.legend(['f(x)=(x+1/3)^2', 'f(x)=(x+1/3)^2'])
	ax.set_xlabel('X Value')
	ax.set_ylabel('f(x)')
	mp.show()


def printSomethingUseful(func, interval, minima):
	fig = mp.figure()
	ax = fig.add_subplot(1, 1, 1)

	x_values = np.linspace(interval[0], interval[1], 100)
	ax.plot(x_values , [func(x) for x in x_values])
	ax.plot(minima[0], minima[1], 'ro')
	ax.annotate(str(minima[0]),(minima[0], minima[1]))

	mp.show()


def goldenSectionFAP(func, interval):

	count = 0
	left = interval[0]
	right = interval[1]

	ml = 0.0
	mr = 0.0

	while (right - left) > 0.0001:
		a = (right - left) * phiPercent
		ml = func(left + a)
		mr = func(right - a)

		print("a " + str(a) + " ml " + str(ml) + " mr " + str(mr))

		count += 1
		if ml < mr:
			right = right - a
		else:
			left = left + a

	# 	print(str(right - left))

	printSomethingUseful(func, interval, (right - (0.5*(right-left)), mr - (0.5*(mr-ml))))

	return left, right

if __name__ == "__main__":
	# Which function shall be used, which interval shall be checked?
	funcToUse = FToAnalyze
	position = (-30, 30)

	# Do it!
	goldenSectionFAP(funcToUse, position)
	# -------------------------------------------------------------- #



