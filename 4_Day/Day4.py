password = "206938"
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