from copy import deepcopy

with open("Day3Input.txt", "r") as input:
	wire1 = [wire.strip() for wire in input.readline().split(",")]
	wire2 = [wire.strip() for wire in input.readline().split(",")]

def generateLineSegs(wire):
	originEndPoint = {"x": 0, "y": 0}
	currentPos = {"x": 0, "y": 0}
	horSegList = []
	verSegList = []

	for segment in wire:
		direction = segment[0]
		magnitude = int(segment[1:len(segment)])

		if direction == "R":
			nextCoord = deepcopy(currentPos)
			nextCoord["x"] += magnitude
			horSegList.append({\
				"x1": currentPos["x"],
				"y1": currentPos["y"],
				"x2": nextCoord["x"],
				"y2": nextCoord["y"]})
			currentPos = deepcopy(nextCoord)

		elif direction == "U":
			nextCoord = deepcopy(currentPos)
			nextCoord["y"] += magnitude
			verSegList.append({\
				"x1": currentPos["x"],
				"y1": currentPos["y"],
				"x2": nextCoord["x"],
				"y2": nextCoord["y"]})
			currentPos = deepcopy(nextCoord)

		elif direction == "L":
			nextCoord = deepcopy(currentPos)
			nextCoord["x"] -= magnitude
			horSegList.append({\
				"x1": nextCoord["x"],
				"y1": nextCoord["y"],
				"x2": currentPos["x"],
				"y2": currentPos["y"]})
			currentPos = deepcopy(nextCoord)

		elif direction == "D":
			nextCoord = deepcopy(currentPos)
			nextCoord["y"] -= magnitude
			verSegList.append({\
				"x1": nextCoord["x"],
				"y1": nextCoord["y"],
				"x2": currentPos["x"],
				"y2": currentPos["y"]})
			currentPos = deepcopy(nextCoord)

	return horSegList, verSegList

horSegList1, verSegList1 = generateLineSegs(wire1)
horSegList2, verSegList2 = generateLineSegs(wire2)

def isIntersecting(horSeg, verSeg):
	x = verSeg["x1"]
	y = horSeg["y1"]

	if (x > horSeg["x1"] and x < horSeg["x2"]) and \
		(y > verSeg["y1"] and y < verSeg["y2"]):
		dist = abs(x) + abs(y)
		return True, ((x, y), dist)
	else:
		return False, ((0, 0), 0)

intersections = []

for horSeg in horSegList1:
	for verSeg in verSegList2:
		result = isIntersecting(horSeg, verSeg)
		if result[0]:
			intersections.append(result[1])


for horSeg in horSegList2:
	for verSeg in verSegList1:
		result = isIntersecting(horSeg, verSeg)
		if result[0]:
			intersections.append(result[1])

distList = []
for point in intersections:
	distList.append(point[1])

distList.sort()
print("Closest Manhatten Distance is: " + str(distList[0]))


