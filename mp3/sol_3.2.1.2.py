import pymd5
import sys
import math
from struct import pack, unpack

# This function generates the padded the MD5 hash uses for a given input string
# It returns a hex string that is only the padding, the input is NOT prepended to the padding.
def padding(string):
    d = string.encode('hex')
    n = int(math.ceil((len(d) * 4) / 512.0)) * 512
    r = n - (len(d) * 4)
    if r < 64:
        r += 512
    p = '1' + ( '0' * (r - 1 - 64))
    h = pack("<q", len(d) * 4).encode('hex')
    return hex(int(p, 2))[2:].replace("L", "") + h

# Open files for reading/get values
with open(sys.argv[1]) as f:
    query = f.readline()

with open(sys.argv[2]) as f:
    command = f.readline()

# Get the base MD5 Hash
token = query.split("user=")[0][6:-1]
print("Input token of: " + token)

# Get length of initial message (query + 8 for password)
lengthData = len("user=" + query.split("user=")[1]) + 8
pad = padding("12345678" + "user=" + query.split("user=")[1])
lengthMessage = lengthData + len(pad)/2

# Create the MD5
attack = pymd5.md5(state=token, count=((lengthData * 8) + len(pad) * 4))
attack.update(command)
print("Generated token of: " + attack.hexdigest())

with open(sys.argv[3], 'w') as f:
    f.write(attack.hexdigest())
