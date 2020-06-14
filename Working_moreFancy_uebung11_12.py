from copy import deepcopy
from time import sleep, perf_counter

filename = "field2.txt"
theHood = [(0,1),(0,-1),(1,0),(-1,0)]
exitPaths = []
counter = [0]

def printMaze(toPrint):
	for a in range(0, len(toPrint)):
		print('|'.join(str(i) for i in toPrint[a]))

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


def inserRoute(route, maze):
	for place in range(len(route)-1):
		if place != 0:
			if route[place+1][1] < route[place][1]:
				maze[route[place][0]][route[place][1]] = "<"
			elif route[place+1][1] > route[place][1]:
				maze[route[place][0]][route[place][1]] = ">"
			elif route[place+1][0] < route[place][0]:
				maze[route[place][0]][route[place][1]] = "^"
			else:
				maze[route[place][0]][route[place][1]] = "v"
		else:
			maze[route[place][0]][route[place][1]] = "S"






def tileState(rowNumber,columnNumber, maze, steps):

	if rowNumber >= 0 and rowNumber < len(maze) and columnNumber >= 0 and columnNumber < len(maze[0]):
			# Exit
			if maze[rowNumber][columnNumber] == 'E':
				return 1
			# Wall
			if maze[rowNumber][columnNumber] == "x":
				return -1
			if maze[rowNumber][columnNumber] == " ":
				maze[rowNumber][columnNumber] = steps
			elif maze[rowNumber][columnNumber] < steps:
				return -1
			else:
				maze[rowNumber][columnNumber] = steps
			return 0

	return -1


def findExitPath(rowNumber, columnNumber, route, visited):
	tile_state = tileState(rowNumber, columnNumber, visited, (len(route)+1))
	route.append((rowNumber, columnNumber))

	if tile_state == 1:
		if len(exitPaths) == 0:
			exitPaths.append(route)
		else:
			if len(exitPaths[0]) >= len(route):
				exitPaths[0] = route

		return 1
	if tile_state == -1:
		return -1
	else:
		for boys in theHood:
			newplace = (route[-1][0] + boys[0],route[-1][1] + boys[1])

			if not (newplace in route):
				findExitPath(newplace[0], newplace[1], deepcopy(route), visited)

	if len(exitPaths) > 0:
		return 1

if __name__ == "__main__":
	start = perf_counter()

	maze = readMaze()
	visited = deepcopy(maze)
	route = []
	foundIt = findExitPath(1, 1, route, visited)
	print(f"foundIt: {foundIt}")
	inserRoute(exitPaths[0], maze)
	print(exitPaths[0])
	printMaze(visited)
	printMaze(maze)
	end = perf_counter()
	print(f"Runtime: {end-start}")
