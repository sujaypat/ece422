import sys
from Crypto.Hash import SHA256

def hamming(sa, sb):
    diffs = 0
    for ca, cb in zip(sa, sb):
        if ca != cb:
            diffs += 1
    return diffs

# Open files
with open(sys.argv[1]) as f:
    fc1 = f.read().strip()
with open(sys.argv[2]) as f:
    fc2 = f.read().strip()

a = bin(int(SHA256.new(fc1).hexdigest(), 16))[2:]
b = bin(int(SHA256.new(fc2).hexdigest(), 16))[2:]

a = a.zfill(max(len(a), len(b)))
b = b.zfill(max(len(a), len(b)))
c = hamming(a, b)

print(str(c))
print(hex(c))

with open(sys.argv[3], "w") as f:
    f.write(str(hex(c)))
