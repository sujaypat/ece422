import sys

def wha(inStr):
    mask = 0x3FFFFFFF
    outHash = 0
    for byte in inStr:
        byte = ord(byte)
        inter_val = ((byte ^ 0xCC) << 24) | ((byte ^ 0x33) << 16) | ((byte ^ 0xAA) << 8) | (byte ^ 0x55)
        outHash = (outHash & mask) + (inter_val & mask)
    return outHash

with open(sys.argv[1]) as f:
    fd = f.read().strip()

with open(sys.argv[2], 'w') as f:
	f.write(format(wha(bytes(fd)), 'x'))
