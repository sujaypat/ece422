import urllib2
import random
import sys
import binascii
import string
from mpi4py import MPI
import math

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

netid = "ptwrdhn2"
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

def break_block(block, previousBlock, rank):
    controlBlock = ""
    controlBlock = '\x00' * 16

    # Make call to oracle with our fakeblock and real ciphertext until padding is correct
    plaintextBlock = ["\x00"] * 16
    for y in reversed(range(0,16)):
        # Store the plaintext as it's being built out
        for x in range(0, 256):
            # Change control block value
            s = list(controlBlock)
            s[y] = chr(x)
            controlBlock = "".join(s)

            # Build the URL to send
            blockHex = binascii.hexlify(block)
            sendData = binascii.hexlify(controlBlock) + blockHex
            urlSend = host + sendData
            #if rank == 0:
            #    print(sendData + " -> (" + str(rank) + ")")

            # Send fake packet
            if get_status(urlSend):
                # Calculate the plaintext value
                previousBlockByte = int(binascii.hexlify(previousBlock[y]), 16)
                expectedByte = ord("\x10")
                plainTextByte = expectedByte ^ previousBlockByte ^ x
                plaintextBlock[y] = chr(plainTextByte)
                #print("Got plaintext of " + hex(plainTextByte) + " on value " + hex(x) + " -> (" + str(rank) + ")")

                # Calculate fixed value, but only if we are not on the last character
                if y != 0:
                    s = list(controlBlock)
                    for z in reversed(range(y,16)):
                        setVal = int(binascii.hexlify(POSSIBLE_PADDINGS_REG[(z-y) + 1]), 16)
                        previousBlockByte = int(binascii.hexlify(previousBlock[z]), 16)
                        fixVal = setVal ^ ord(plaintextBlock[z]) ^ previousBlockByte
                        s[z] = chr(fixVal)
                    controlBlock = "".join(s)
                    #print("Locked control block to " + binascii.hexlify(controlBlock) + " -> (" + str(rank) + ")")
                break

    return filter(lambda x: x in string.printable, "".join(plaintextBlock)).strip()
    

# Read data in
with open("3.2.3_ciphertext.hex") as f:
    data = f.readline()

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

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

if rank == 0:
    # This just exists to make sure I didn't mess up spliting/converting the data
    print("Number of blocks: " + str(len(dblocks)))
    print("Conducting sanity check....")
    u = host + binascii.hexlify("".join(dblocks))
    if not get_status(u):
        print("Sanity check failed! Clinically insane!")
        # Kill the thread group
        comm.Abort(-1)
    print("Passed...")

# Wait for all threads...
comm.Barrier()

# So we can attack the last block first
dblocks.reverse()

decodedValue = [""] * len(dblocks)

for b in range(0, int(math.ceil(float(len(dblocks))/size))):
    if rank == 0:
        print("On round " + str(b) + " of " + str(int(math.ceil(float(len(dblocks))/size))))

    comm.Barrier()
    bNum = (b * size) + rank

    if bNum < (len(dblocks) - 1):
        print("Rank " + str(rank) + " starting on block " + str(bNum) + " (" + binascii.hexlify(dblocks[bNum])  +") with previous block " + str(bNum + 1) + " (" + binascii.hexlify(dblocks[bNum + 1]) + ")")
        val = break_block(dblocks[bNum], dblocks[bNum + 1], rank)
        print("Rank " + str(rank) + " got value: " + val.strip())
    else:
        print("Rank " + str(rank) + " sleeping...")
        val = ""

    if rank == 0:
        decodedValue[len(decodedValue) - bNum - 1] = val
        for i in range(1, size):
            data = comm.recv(source = i, tag = 11)
            idx = (b * size) + i
            if idx < len(decodedValue):
                decodedValue[len(decodedValue) - idx - 1] = data
    else:
        comm.send(val, dest = 0, tag = 11)
    
    if rank == 0:
        print("Results after round: " + "".join(decodedValue).strip())


# Wait for everyone to finish decrypting
comm.Barrier()

if rank == 0:
    with open("sol_3.2.3.txt", 'w') as f:
        f.write("".join(decodedValue).strip())
