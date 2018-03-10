from Crypto.Cipher import AES

key = 0
cipher  = 'c0411e894f1b0535d384cd66524a77861cf11de371325616cb57e090c9fed21899d6cf924fbe06032f09b0996e447a15a67d3863cbeea7e6d004c5edcab2f8a55126498a293ec5ea014d6fc3612f76f5'
iv = ('%032X' % 0).decode('hex')

for i in range(32):
	print(('%064X' % i))
	aes = AES.new(key=('%064X' % i).decode('hex'),
				  mode=AES.MODE_CBC,
				  IV=iv)
	try:
		print(aes.decrypt(cipher.decode('hex')).decode('ascii'))
	except:
		pass
