import csv
import copy

inputFilename = "Day2Input.txt"


with open(inputFilename, "r") as intcode:
	intcodeArray = [op.strip() for op in intcode.read().split(",")]
#Initialize all as integers
intcodeArray = [int(element) for element in intcodeArray]
part2IntcodeArray = copy.deepcopy(intcodeArray)
#Set programming
intcodeArray[1] = 12
intcodeArray[2] = 2

def RunProgram(intcodeArray):
	position = 0 
	opcode = intcodeArray[position] 
	while (True): 
		if opcode == 1:
			intcodeArray[intcodeArray[position + 3]] = intcodeArray[intcodeArray[position+ 1]] + intcodeArray[intcodeArray[position + 2]] 
		elif opcode == 2:
			intcodeArray[intcodeArray[position + 3]] = intcodeArray[intcodeArray[position+ 1]] * intcodeArray[intcodeArray[position + 2]] 
		elif opcode == 99: 
			break
		else: 
			print("You shouldn't be here")
			break
		position += 4 
		opcode = intcodeArray[position]

RunProgram(intcodeArray)

print("Part 1 Answer: "+ str(intcodeArray[0]))


#Part 2

def FindProgram(intcodeArray, endValue):
	tempIntcodeArray = copy.deepcopy(intcodeArray)
	for n in range (0, 99):
		for v in range(0, 99):
			tempIntcodeArray[1] = n
			tempIntcodeArray[2] = v
			RunProgram(tempIntcodeArray)
			if tempIntcodeArray[0] == endValue:
				return n, v
			tempIntcodeArray = copy.deepcopy(intcodeArray)

tempIntcodeArray = copy.deepcopy(part2IntcodeArray)
print(FindProgram(tempIntcodeArray, 19690720))


print(tempIntcodeArray)