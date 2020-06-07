import sorting as sa
import time
import numpy as np
import matplotlib.pyplot as mp
from copy import deepcopy

def printResults(times):
	colors = ["green", "red", "cyan", "magenta", "black", "blue"]
	fig = mp.figure()
	ax = fig.add_subplot(1, 1, 1)

	if len(times) > len(colors):
		return -1
	else:
		for x in times:
			x_values = []
			y_values = []
			for c in x:
				x_values.append(c[0])
				y_values.append(c[1])
			ax.loglog(x_values, y_values)
			ax.set_color = colors.pop()
		mp.show()

def testListsGenerator(listCount: int, maxLength: int, lowhigh:int ):
	"""
	listCount = Number of lists to be generated
	maxLength = Maximum length of last list

	The lenght of each list will be equally spaced from 3 items to maxLength

	"""

	generatedLists = []

	if (maxLength > 0):
		items = int (maxLength / listCount)
		if items > 1:
			for i in range(1,(listCount +1)):
				generatedLists.append((np.random.randint(lowhigh[0], lowhigh[1], items*i)).tolist())
		else:
			for i in range(1,(maxLength +1)):
				generatedLists.append((np.random.randint(lowhigh[0], lowhigh[1], i)).tolist())
		return generatedLists

def SortTest(algorithm, toSort):

	times = []
	for x in algorithm:
		algTime = []
		for c in toSort :
			start = time.perf_counter()
	#		sortedArr.append(sa.bubbleSort(c))
			c = x(deepcopy(c))
			end = time.perf_counter()
			algTime.append((len(c),(end-start)))
		times.append(algTime)
	return times





if __name__ == "__main__":
	sortTime = []
	toSort = testListsGenerator(30, 1000, (0,100))
	sortTime = SortTest([sa.bubbleSort, sa.insertionSort, sa.selectionSort], toSort)

	printResults(sortTime)











