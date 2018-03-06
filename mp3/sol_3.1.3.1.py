import sys
from Crypto.Hash import SHA256

def hamming(sa, sb):
    diffs = 0
    for ca, cb, in zip(sa, sb):
        if ca != cb:
            diffs += 1
    return diffs

# Open files
with open(sys.argv[1]) as f:
    fc1 = f.read().strip()
with open(sys.argv[2]) as f:
    fc2 = f.read().strip()

h = SHA256.new()
h.update(fc1)
a = h.hexdigest()
h.update(fc2)
b = h.hexdigest()
c = hamming(a, b)

with open(sys.argv[3], "w") as f:
    f.write(str(c))
