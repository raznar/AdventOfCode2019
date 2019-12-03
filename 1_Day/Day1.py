#!/usr/bin/python3
import math

part1InputFile = "Day1Part1-Input.txt"
massArray = []
with open(part1InputFile, "r") as inputText:
	for mass in inputText:
		massArray.append(math.floor(int(mass)/3) - 2)

totalFuel = 0
for fuel in massArray:
	totalFuel += fuel

print("Part 1 Total Fuel: " + str(totalFuel))


#Part 2
additionalFuel = []
with open(part1InputFile, "r") as moduleMass:
	for mass in moduleMass:
		tempFuel = int(mass)
		while (tempFuel > 0):
			tempFuel = math.floor(tempFuel / 3) - 2
			if tempFuel > 0:
				additionalFuel.append(tempFuel)

totalFuel = 0
for fuel in additionalFuel:
	totalFuel += fuel

print("Part 2 Total Fuel: " + str(totalFuel))