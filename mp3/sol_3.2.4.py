import struct
import re
import mpi4py
from operator import mul
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import AES, PKCS1_v1_5

e = 65537
ciphertext = RSA.importKey("""-----BEGIN PRETTY BAD ENCRYPTED MESSAGE-----
gAAAAEFe1XK++19nHNZD4UJAuJqVTPbgRxP5fpXjydnyWss3HhuKla/Kl6Ap2ngMIYQioDwCOaob
fDxlQQ7xwftvHdxRFCUeLO1cpxlLnyzYQac1yHvnHGGo16hYG0JGyldvITHsVWNQla53C/YakR2h
Oukjr4I18sNTomS9upyz/p8AHox/MbxCvap3yGNQjt/XrMbaSzXXCAkzJ7H7QguVEmWdEU0RqgRO
430kpH+jXHDw0tinQ+QA0sN1pJlKxb1g6KkJjYQNcjS2RrfCOitn+143LUTxT38EmRfEDKvKF0lm
1zX2JXpD+oMDUBM732U6spLlX6JnyVY9Byh4/r+wkWBwQeeQSl/GWOsEu2xVQ4enJcHMhuyZJwOP
2K76ndl2Ng==
-----END PRETTY BAD ENCRYPTED MESSAGE-----
""")

def product(X):
	if len(X) == 0:
		return 1
	while len(X) > 1:
		X = [reduce(mul, X[i*2:(i+1)*2], 1) for i in range((len(X)+1)/2)]
		print(len(X))
	return X[0]

def producttree(X):
	result = [X]
	while len(X) > 1:
		X = [reduce(mul, X[i*2:(i+1)*2], 1) for i in range((len(X)+1)/2)]
		result.append(X)
	return result

def remainders_using_product_tree(n,T):
	result = [n]
	for t in reversed(T):
		result = [result[floor(i/2)] % t[i] for i in range(len(t))]
	return result

def remainders(n,X):
	return remainders_using_product_tree(n,producttree(X))

def find_gcd(moduli):
	prod = product(moduli)
	rem = remainders(50000, prod)
	# return rem


keys = []

with open('moduli.hex', 'r') as moduluses_af:
	for line in moduluses_af:
		keys.append(int(line.rstrip(), 16))

with open('3.2.4_ciphertext.enc.asc', 'r') as garbage:
	pass

pkeys = find_gcd(keys)
for p in pkeys:
	print(pbp.decrypt(RSA.construct((p, long(e), long(d)).exportKey()), cipertext))
