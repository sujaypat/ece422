import struct
import re
import mpi4py
import pbp

from fractions import gcd
from operator import mul

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import AES, PKCS1_v1_5

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def lcm(a, b):
    return (a * b) // gcd(a, b)

def findPrivateExponent(gcd, moduli):
    return modinv(65537, (gcd - 1) * ((moduli // gcd) - 1))
    
def pTree(values):
    print("Computing product tree...")
    ret = [values]
    while len(values) > 1:
        print(len(values))
        values = [reduce(mul, values[(i * 2):((i + 1) * 2)], 1) for i in range((len(values) + 1) / 2)]
        ret.append(values)
    print("Done computing product tree...")
    return ret

def rTree(productTree):
    print("Computing remainder tree...")
    remainders = productTree.pop()
    while productTree:
        div = productTree.pop()
        print(len(remainders), len(div))
        remainders = [remainders[i / 2] % div[i] ** 2 for i in range(len(div))]
    print("Done computing remainder tree...")
    return remainders, div

def fastGCD(keys):
    r, d = rTree(pTree(keys))
    return [gcd(r / n, n) for r, n in zip(r, d)]


keys = []

with open('moduli.hex', 'r') as f:
    for line in f:
        keys.append(int(line.rstrip(), 16))

with open('3.2.4_ciphertext.enc.asc', 'r') as f:
    ciphertext = "".join(f.readlines())

gcds = fastGCD(keys)

print(len(gcds))

for i in range(len(gcds)):
    if gcds[i] != 1:
        d = findPrivateExponent(gcds[i], keys[i])
        key = RSA.construct( (long(keys[i]), long(65537), long(d)) )
        try:
            print pbp.decrypt(key, ciphertext)
        except ValueError:
            pass
