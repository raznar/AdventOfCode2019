import csv

inputFilename = "Day2Input.txt"

with open(inputFilename, "r") as intcode:
	intcodeArray = [op.strip() for op in intcode.read().split(",")]
#Initialize all as integers
intcodeArray = [int(element) for element in intcodeArray]
#Set programming
intcodeArray[1] = 12
intcodeArray[2] = 2

print(intcodeArray)

position = 0
opcode = intcodeArray[position]
while (True):
	if opcode == 1:
		intcodeArray[position + 3] = intcodeArray[position + 1] + intcodeArray[position + 2]
	elif opcode == 2:
		intcodeArray[position + 3] = intcodeArray[position + 1] * intcodeArray[position + 2]
	elif opcode == 99:
		break
	else:
		print("You shouldn't be here")
	position += 4
	opcode = intcodeArray[position]

print(intcodeArray)