import sys
from Crypto.Cipher import AES

def read_key():
	key = ''
	iv = ''

	with open(sys.argv[2], 'r') as f:
		key = f.readline()

	with open(sys.argv[3], 'r') as f:
		iv = f.readline()

	return (key.decode('hex'), iv.decode('hex'))

def translate():
	to_uncipher = ''
	key, iv = read_key()

	with open(sys.argv[1], 'r') as f:
		to_uncipher = f.readline()

	aes = AES.new(key=key, mode=AES.MODE_CBC, IV=iv)
	result = aes.decrypt(to_uncipher.decode('hex'))

	with open(sys.argv[4], 'w') as f:
		f.write(result)


translate()
