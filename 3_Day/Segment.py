from copy import deepcopy

with open("TestInput.txt", "r") as input:
	wire1 = [wire.strip() for wire in input.readline().split(",")]
	wire2 = [wire.strip() for wire in input.readline().split(",")]

def generateLineSegs(wire):
	segList = []
	originEndPoint = {"x": 0, "y": 0}

	for segment in wire:
		direction = segment[0]
		