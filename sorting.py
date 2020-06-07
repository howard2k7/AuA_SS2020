def bubbleSort(toSort):

	# If Array got only 1 item it is sorted anyways..
	if len(toSort) <= 1:
		return toSort

	# Anything "changed" in the last run?
	# Every iteration, we know the last "runCounter"-1 Items are sorted
	changed = 1
	runCounter = 1

	while changed:
		changed = 0

		# Bubble the greatest to the End
		for i in range(0,len(toSort)-runCounter):
			if toSort[i] > toSort[i+1]:
				toSort[i], toSort[i+1] = toSort[i+1], toSort[i]
				changed = 1

		runCounter = runCounter + 1

	return toSort


def insertionSort(toSort):

	# If Array got only 1 item it is sorted anyways..
	if len(toSort) <= 1:
		return toSort

	# Messy but works, could be 1 add Register lockup faster then the not messy Version
	for i in range(1,len(toSort)):
		value = toSort[i]
		for j in range(i-1, -1, -1):
			if value < toSort[j]:
				if j == 0:
					toSort[j + 1] = toSort[j]
					toSort[j] = value
				else:
					toSort[j+1] = toSort[j]
					i = i - 1
			else:
				toSort[i] = value
	return toSort


def selectionSort(toSort):

	# If Array got only 1 item it is sorted anyways..
	if len(toSort) <= 1:
		return toSort

	for i in range (0,(len(toSort)-1)):
		min = i
		for j in range(i+1,len(toSort)):
			if toSort[j] < toSort[min]:
				min = j
		toSort[i], toSort[min] = toSort[min], toSort[i]
	return toSort


if __name__ == "__main__":
	print(bubbleSort([3, 4, 2, 1, 6, 5]))




