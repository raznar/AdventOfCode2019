from copy import deepcopy

with open("TestInput.txt", "r") as input:
	wire1 = [wire.strip() for wire in input.readline().split(",")]
	wire2 = [wire.strip() for wire in input.readline().split(",")]


def directionToCoord(wire):
	coordList = []
	origin = {"x": 0, "y": 0}
	coordList.append(origin)

	currentPos = {"x":0, "y":0}

	for line in wire:
		direction = line[0]

		magnitude = int(line[1:len(line)])

		if direction == "R":
			for point in range(0, magnitude):
				currentPos["x"] += 1
				tempCoord = deepcopy(currentPos)
				coordList.append(tempCoord)

		elif direction == "U":
			for point in range(0, magnitude):
				currentPos["y"] += 1
				tempCoord = deepcopy(currentPos)
				coordList.append(tempCoord)

		elif direction == "L":
			for point in range(0, magnitude):
				currentPos["x"] -= 1
				tempCoord = deepcopy(currentPos)
				coordList.append(tempCoord)

		elif direction == "D":
			for point in range(0, magnitude):
				currentPos["y"] -= 1
				tempCoord = deepcopy(currentPos)
				coordList.append(tempCoord)

		else:
			print("You shouldn't be here")

	return coordList





coordList1 = directionToCoord(wire1)
coordList2 = directionToCoord(wire2)
print(coordList1)
print(coordList2)