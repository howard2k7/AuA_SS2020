from copy import deepcopy

filename = "field2.txt"
theHood = [(0,1),(0,-1),(1,0),(-1,0)]
exitPaths = []

def printMaze(toPrint):
    for a in range(0, len(toPrint)):
        print(''.join(str(i) for i in toPrint[a]))

def readMaze():
	newMaze = []
	with open(filename) as fp:
		line = fp.readline()
		count = 0
		while line:
			newMaze.append([])
			line = line.strip('\n')
			for i in line:
				newMaze[count].append(i)
			line = fp.readline()
			count += 1
	return newMaze

def tileState(rowNumber,columnNumber, maze):
	#print(f"tilestate {rowNumber} {columnNumber} the is:{maze[rowNumber][columnNumber]}")
	if rowNumber >= 0 and rowNumber < len(maze) and columnNumber >= 0 and columnNumber < len(maze[0]):
			# Exit
			if maze[rowNumber][columnNumber] == 'E':
				return 1
			# Wall
			if maze[rowNumber][columnNumber] == "x":
				print("X")
				return -1
			return 0
	print("OOB")
	return -1


def findExitPath(rowNumber, columnNumber, route, maze):
	tile_state = isFree(rowNumber, columnNumber, maze)
	print(f"Equals {tile_state}")
	route.append((rowNumber, columnNumber))
	if tile_state == 1:
		exitPaths.append(route)
		return 1
	if tile_state == -1:
		return -1
	else:
		for boys in theHood:
			beenThere = False
			print(f"boys: {boys}")
			print(f"route: {route[-1]}")
			#print(route[-1])
			newplace = (route[-1][0] + boys[0],route[-1][1] + boys[1])
			print(f"newplace: {newplace}")
			for i in route:
				if i == newplace:
					#print("broken")
					beenThere = True
			if beenThere == False:

				found = findExitPath(newplace[0], newplace[1], deepcopy(route), maze)
				if found == 1:
					return 1


if __name__ == "__main__":
	isFree = tileState
	maze = readMaze()
	route = []
	printMaze(maze)
	foundIt = findExitPath(1,1,route, maze)
	print(f"foundIt: {foundIt}")
	print(exitPaths)