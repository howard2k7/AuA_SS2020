from copy import deepcopy
from time import sleep, perf_counter

filename = "field3.txt"
#theHood = [(0,1),(0,-1),(1,0),(-1,0)]
theHood = [(0,-1),(1,0),(-1,0),(0,1)]
exitPaths = []
directNeigbours = []
counter = 0

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


def isFree(place):
	if place[0] >= 0 and place[0] < len(maze) and place[1] >= 0 and place[1] < len(maze[0]):
		if maze[place[0]][place[1]] == 'x':
			return False
		return True
	return False


def findExitPath(rowNumber, columnNumber, route, visited):
	global counter
	route.append((rowNumber, columnNumber))

	if visited[rowNumber][columnNumber] == 'E':
		counter = counter + 1
		if len(exitPaths) == 0:
			exitPaths.append(route)
		else:
			print(f"Found {counter}")
			if len(exitPaths[0]) >= len(route):
				exitPaths[0] = route
	else:
		for boys in theHood:
			newplace = (route[-1][0] + boys[0],route[-1][1] + boys[1])#

			if (not (newplace in route)) and (isFree(newplace)):
				if (not (newplace in directNeigbours)):
					directNeigbours.append(newplace)
					findExitPath(newplace[0], newplace[1], deepcopy(route), visited)
	if len(exitPaths) > 0:
		return 1
	return 0

if __name__ == "__main__":
	start = perf_counter()

	maze = readMaze()
	visited = deepcopy(maze)
	route = []
	foundIt = findExitPath(1, 1, route, visited)
	print(f"foundIt: {foundIt}")
	inserRoute(exitPaths[0], maze)
	print(exitPaths[0])
	printMaze(maze)
	end = perf_counter()
	print(f"Runtime: {end-start}")
