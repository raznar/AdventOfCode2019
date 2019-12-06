from copy import deepcopy

with open("TestInput.txt", "r") as input:
	wire1 = [wire.strip() for wire in input.readline().split(",")]
	wire2 = [wire.strip() for wire in input.readline().split(",")]

def generateLineSegs(wire):
	segList = []
	originEndPoint = {"x": 0, "y": 0}
	currentPos = {"x": 0, "y": 0}

	for segment in wire:
		direction = segment[0]
		magnitude = int(segment[1:len(segment)])

		if direction == "R":
			nextCoord = deepcopy(currentPos)
			nextCoord["x"] += magnitude
			segList.append({\
				"x1": currentPos["x"],
				"y1": currentPos["y"],
				"x2": nextCoord["x"],
				"y2": nextCoord["y"]})
			currentPos = deepcopy(nextCoord)

		elif direction == "U":
			nextCoord = deepcopy(currentPos)
			nextCoord["y"] += magnitude
			segList.append({\
				"x1": currentPos["x"],
				"y1": currentPos["y"],
				"x2": nextCoord["x"],
				"y2": nextCoord["y"]})
			currentPos = deepcopy(nextCoord)

		elif direction == "L":
			nextCoord = deepcopy(currentPos)
			nextCoord["x"] -= magnitude
			segList.append({\
				"x1": currentPos["x"],
				"y1": currentPos["y"],
				"x2": nextCoord["x"],
				"y2": nextCoord["y"]})
			currentPos = deepcopy(nextCoord)

		elif direction == "D":
			nextCoord = deepcopy(currentPos)
			nextCoord["y"] -= magnitude
			segList.append({\
				"x1": currentPos["x"],
				"y1": currentPos["y"],
				"x2": nextCoord["x"],
				"y2": nextCoord["y"]})
			currentPos = deepcopy(nextCoord)

	print(segList)

print(wire1)
generateLineSegs(wire1)