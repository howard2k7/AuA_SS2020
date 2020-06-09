import sorting as sa
import time
import numpy as np
import matplotlib.pyplot as mp
from copy import deepcopy
import concurrent.futures

def printResults(times, sortieralgorithmen, plotart):
	"""
	Generates a graphical visualization of the runtimes {times} needed
	by the algorithms {sortieralgorithmen} using a defined plot type {plotart}
	"""
	colors = ["green", "red", "cyan", "magenta", "black", "blue"]
	if len(times) > len(colors):
		return -1
	lbls = []
	for lbl in sortieralgorithmen:
		lbls.append(lbl.__name__)
	myPlots = []
	for x in times:
		x_values = []
		y_values = []
		for i in x:
			x_values.append(i[0])
			y_values.append(i[1])
		myPlots.append(plotart(x_values, y_values, color = colors.pop()))
	mp.legend(lbls)
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
	"""
	Sorts the lists in {toSort} with all algorithm functions in {algorithm}
	"""
	times = []
	for x in algorithm:
		algTime = []
		for c in toSort :
			start = time.perf_counter()
			c = x(deepcopy(c))
			end = time.perf_counter()
			algTime.append((len(c),(end-start)))
		times.append(algTime)
	return times


def SingleSortTest(args):
	"""
	Helper function for multiprocessor sorting
	{args}: [0] function used for sorting
			[1] list of unsorted lists
	"""
	algTime = []
	for c in args[1] :
		start = time.perf_counter()
		c = args[0](c)
		end = time.perf_counter()
		algTime.append((len(c),(end-start)))
	return algTime


def SortMultiCPU(algorithm, toSort):
	"""
	Sorts the lists in {toSort} with all algorithm functions in {algorithm}, but with multiple CPUs
	"""
	args = [(x,deepcopy(toSort)) for x in algorithm]
	with concurrent.futures.ProcessPoolExecutor() as executor:
		runtimes = executor.map(SingleSortTest, args)

	return list(runtimes)


if __name__ == "__main__":
	sortTime = []
	"""
	Setup:	
	__________________________________________________________________________
	"""
	sortieralgorithmen = [sa.bubbleSort, sa.insertionSort, sa.selectionSort]
	plotart = mp.loglog
	anzahlListen = 1000
	maximaleListenlaenge = 1000
	wertebereich = (0, 100)
	multiprocessor = 1
	"""_______________________________________________________________________
	"""

	begin = time.perf_counter()
	toSort = testListsGenerator(anzahlListen, maximaleListenlaenge, wertebereich)

	if multiprocessor == 0:
		sortTime = SortTest(sortieralgorithmen, toSort)
	else:
		sortTime = SortMultiCPU(sortieralgorithmen,toSort)

	printResults(sortTime, sortieralgorithmen, plotart)

	end = time.perf_counter()
	print(f'Programmausführung in {end-begin}')











