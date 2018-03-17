import urllib2
import random
import sys
import binascii

POSSIBLE_PADDINGS = ['\x10',
        '\x0f',
        '\x0e',
        '\x0d',
        '\x0c',
        '\x0b',
        '\x0a',
        '\x09',
        '\x08',
        '\x07',
        '\x06',
        '\x05',
        '\x04',
        '\x03',
        '\x02',
        '\x01']

POSSIBLE_PADDINGS_REG = ['\x10',
        '\x0f',
        '\x0e',
        '\x0d',
        '\x0c',
        '\x0b',
        '\x0a',
        '\x09',
        '\x08',
        '\x07',
        '\x06',
        '\x05',
        '\x04',
        '\x03',
        '\x02',
        '\x01']

POSSIBLE_PADDINGS.reverse()

netid = "tdubey3"
host = 'http://72.36.89.11:9999/mp3/' + netid + '/?'

# ONLY USE WHEN TESTING LOCALLY
hostTest = 'http://127.0.0.1:8081/mp3/test/'

def get_status(u):
    req = urllib2.Request(u)
    try:
        f = urllib2.urlopen(req)
        return True
    except urllib2.HTTPError, e:
        if e.code == 404:
            return True
        return False

# Read data in
with open("3.2.3_ciphertext.hex") as f:
    data = f.readline()
print("Data of length " + str(len(data)/2) + " bytes read.")

# Split data into 128-bit (16 byte) blocks
dblocks = []
sBuild = ""
count = 0
for x in data:
    sBuild += x
    count = count + 1
    if count >= 32:
        dblocks.append(sBuild)
        count = 0
        sBuild = ""
dblocks = [binascii.unhexlify(x) for x in dblocks]


# This just exists to make sure I didn't mess up spliting/converting the data
print("Conducting sanity check....")
u = host + binascii.hexlify("".join(dblocks))
if not get_status(u):
    print("Sanity check failed! Clinically insane!")
    sys.exit(-1)
print("Passed...")

# So we can attack the last block first
dblocks.reverse()

# Generate a block of "ciphertext" that is all zeroes
# Last bit is all zeores as that's what we change
controlBlock = ""
controlBlock = '\x00' * 16

print("Generated fakeblock of: " + controlBlock.encode('hex'))
print("Block to crack is:      " + dblocks[0].encode('hex'))
print("Starting...")


# Make call to oracle with our fakeblock and real ciphertext until padding is correct
plaintextBlock = []
for y in reversed(range(0,16)):
    # Store the plaintext as it's being built out
    for x in range(0, 256):
        # Change control block value
        s = list(controlBlock)
        s[y] = chr(x)
        controlBlock = "".join(s)

        # Build the URL to send
        blockHex = binascii.hexlify(dblocks[0])
        sendData = binascii.hexlify(controlBlock) + blockHex
        urlSend = host + sendData

        # Print for debugging
        sys.stdout.write("%s\r" % sendData)
        sys.stdout.flush()

        # Send fake packet
        if get_status(urlSend):
            # Calculate the plaintext value
            previousBlockByte = int(binascii.hexlify(dblocks[1][y]), 16)
            plainTextByte = int(binascii.hexlify(POSSIBLE_PADDINGS[y]), 16) ^ previousBlockByte ^ x
            plaintextBlock = [plainTextByte] + plaintextBlock
            print("")
            print("Found value: " + hex(x) + " with plaintext of " + hex(plainTextByte))

            # Calculate fixed value
            s = list(controlBlock)
            for z in reversed(range(y,16)):
                setVal = int(binascii.hexlify(POSSIBLE_PADDINGS_REG[z-y]), 16)
                previousBlockByte = int(binascii.hexlify(dblocks[1][z]), 16)
                fixVal = setVal ^ plainTextByte ^ previousBlockByte
                print(hex(setVal), hex(previousBlockByte), hex(fixVal), z)
                s[z] = chr(fixVal)
            controlBlock = "".join(s)
            print("Locked control block to: " + binascii.hexlify(controlBlock))
            break
