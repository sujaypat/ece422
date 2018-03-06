#!bin/python
from bottle import request, route, response, run
from Crypto.Cipher import AES
from Crypto import Random

# Pad the message to a multiple of 16 bytes
def pad(msg):
    n = len(msg)%16
    return msg + ''.join(chr(i) for i in range(16,n,-1))

# Remove the padding, returning an error if bad padding 
def strip_padding(msg):
    padlen = 17 - ord(msg[-1])
    if padlen > 16 or padlen < 1:
        return True, None
    if msg[-padlen:] != ''.join(chr(i) for i in range(16,16-padlen,-1)):
        return True, None
    return False, msg[:-padlen]

# Encrypt the messages using CBC mode
def enc(key,msg):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(pad(msg))

# Decrypt the message using CBC mode
def dec(msg):
    cipher = AES.new(key, AES.MODE_CBC, msg[:16])
    text = cipher.decrypt(msg[16:])
    return text

# Example encryption  the real server encrypts using your solution
# using a random key and iv (different for each user)
key = 'ECE422SP2017 key'
plaintext = 'Be sure to drink your Ovaltine!'
print pad(plaintext).encode('hex'), len(pad(plaintext))
ciphertext = enc(key, plaintext)
print 'ciphertext:', ciphertext.encode('hex')

@route('/mp3/test/<name>')
def index(name):
    q = name
    try:
        msg = dec(q.decode('hex'))
        if msg == "":
            response.status = 500
            return "Ciphertext is empty\n"
        (err, msg) = strip_padding(msg)
        if err:
            response.status = 500
            return "Padding error\n"
        else:
            if msg == plaintext:
                return "Correct ciphertext!\n"
            else:
                response.status = 404
                return "Incorrect ciphertext!\n"
            
    except Exception, e:
        response.status = 500
        return e.message

if  __name__ == '__main__':
    run(port=8081)
