from copy import deepcopy

with open("Day3Input.txt", "r") as input:
	wire1 = [wire.strip() for wire in input.readline().split(",")]
	wire2 = [wire.strip() for wire in input.readline().split(",")]

def generateLineSegs(wire):
	originEndPoint = {"x": 0, "y": 0}
	currentPos = {"x": 0, "y": 0}
	horSegList = []
	verSegList = []
	distTraveled = 0

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
				"y2": nextCoord["y"],
				"distTraveled": distTraveled,
				"dir": 0})
			distTraveled += magnitude
			currentPos = deepcopy(nextCoord)

		elif direction == "U":
			nextCoord = deepcopy(currentPos)
			nextCoord["y"] += magnitude
			verSegList.append({\
				"x1": currentPos["x"],
				"y1": currentPos["y"],
				"x2": nextCoord["x"],
				"y2": nextCoord["y"],
				"distTraveled": distTraveled,
				"dir": 0})
			distTraveled += magnitude
			currentPos = deepcopy(nextCoord)

		elif direction == "L":
			nextCoord = deepcopy(currentPos)
			nextCoord["x"] -= magnitude
			horSegList.append({\
				"x1": nextCoord["x"],
				"y1": nextCoord["y"],
				"x2": currentPos["x"],
				"y2": currentPos["y"],
				"distTraveled": distTraveled,
				"dir": 1})
			distTraveled += magnitude
			currentPos = deepcopy(nextCoord)

		elif direction == "D":
			nextCoord = deepcopy(currentPos)
			nextCoord["y"] -= magnitude
			verSegList.append({\
				"x1": nextCoord["x"],
				"y1": nextCoord["y"],
				"x2": currentPos["x"],
				"y2": currentPos["y"],
				"distTraveled": distTraveled,
				"dir": 1})
			distTraveled += magnitude
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

		totalSteps = horSeg["distTraveled"] + verSeg["distTraveled"]
		if horSeg["dir"] == 0:
			totalSteps += abs(x-horSeg["x1"])
		else:
			totalSteps += abs(x-horSeg["x2"])
		if verSeg["dir"] == 0:
			totalSteps += abs(y-verSeg["y1"])
		else:
			totalSteps += abs(y-verSeg["y2"])

		return True, ((x, y), dist, totalSteps)
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

manDistList = []
stepDistList = []
for point in intersections:
	manDistList.append(point[1])
	stepDistList.append(point[2])

manDistList.sort()
stepDistList.sort()
print("Closest Manhatten Distance is: " + str(manDistList[0]))
print("Closest Intersection by Steps is: " + str(stepDistList[0]))

