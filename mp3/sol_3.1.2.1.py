import sys

translation = {}

def read_key():
	cipher_alpha = ''

	with open(sys.argv[2], 'r') as f:
		cipher_alpha += f.readline()

	for i in range(len(cipher_alpha)):
		translation[cipher_alpha[i]] = chr(ord('A')+ i)

def translate():
	to_uncipher = ''

	with open(sys.argv[1], 'r') as f:
		to_uncipher += f.readline()

	result = ''
	for i in range(len(to_uncipher)):
		if to_uncipher[i].isdigit() or to_uncipher[i].isspace():
			result += to_uncipher[i]
		else:
			result += translation[to_uncipher[i]]

	with open(sys.argv[3], 'w') as f:
		f.write(result)

read_key()
translate()
