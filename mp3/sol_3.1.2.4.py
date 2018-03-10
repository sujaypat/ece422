import sys

def read():
	cipher = 0
	pkey = 0
	modulo = 0

	with open(sys.argv[1], 'r') as fuck:
		cipher = int(fuck.readline(), 16)

	with open(sys.argv[2], 'r') as shit:
		pkey = int(shit.readline(), 16)

	with open(sys.argv[3], 'r') as yasha:
		modulo = int(yasha.readline(), 16)

	return(cipher, pkey, modulo)

def some_shit():
	cipher, pkey, modulo = read()

	result = hex(pow(cipher, pkey, modulo))[2:].replace('L', '')

	with open(sys.argv[4], 'w') as kms:
		kms.write(result)

some_shit()
