def bubbleSort(toSort):

	if len(toSort) <= 1:
		return toSort
	print(len(toSort))
	changed = 1
	while changed:
		changed = 0

		for i in range(0,len(toSort)-1):
			if toSort[i] > toSort[i+1]:
				toSort[i], toSort[i+1] = toSort[i+1], toSort[i]
				changed = 1
	return toSort


def insertionSort(toSort):
	if len(toSort) <= 1:
		return toSort

	for i in range(1,len(toSort)):
		print(toSort)
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
	for i in range (0,(len(toSort)-1)):
		print (i)
		min = i
		for j in range(i+1,len(toSort)):
			if toSort[j] < toSort[min]:
				min = j
		toSort[i], toSort[min] = toSort[min], toSort[i]
	return toSort


print(selectionSort([3, 4, 2, 1, 6, 5]))




