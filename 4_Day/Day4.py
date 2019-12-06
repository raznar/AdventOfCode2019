validPassword = 0

def validatePassword(pw):
	for i in range(len(pw) - 1):
		if pw[i] > pw[i + 1]:
			return False

	containsDouble = False
	for i in range(len(pw) - 1):
		if pw[i] == pw[i + 1]:
			containsDouble = True

	return containsDouble

for i in range(206938, 679128):
	if validatePassword(str(i)):
		validPassword += 1

print("Number of Valid Passwords from 206938 to 679128: " + str(validPassword))

def validatePasswordP2(pw):
	for i in range(len(pw) - 1):
		if pw[i] > pw[i + 1]:
			return False

	containsDouble = False
	for i in range(len(pw) - 1):
		if pw[i] == pw[i + 1]: 
			if pw.count(pw[i]) == 2:
				return True

	return containsDouble

validPasswordP2 = 0
for i in range(206938, 679128):
	if validatePasswordP2(str(i)):
		validPasswordP2 += 1

print("P2: Number of Valid Passwords from 206938 to 679128: " + str(validPasswordP2))