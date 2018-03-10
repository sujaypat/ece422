from Crypto.Hash import MD5
import sys

def padding(string):
    d = string.encode('hex')
    print(len(d) * 4)
    print(int(512 * round(float((len(d) * 4))/512)))
    s = len(d) * 8
    r = 512 - s%512
    print(r)
    print((len(d) * 4) + r)
    if r < 64:
        r += 512
    p = '1' + ( '0' * (r - 1 - 64)) + format(r, '064b')
    return hex(int(p, 2))[2:]


with open(sys.argv[1]) as f:
    query = f.readline()

with open(sys.argv[2]) as f:
    command = f.readline()

u = padding(query)

