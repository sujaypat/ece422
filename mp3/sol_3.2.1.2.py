import sys, io
from pymd5 import md5, padding
from urllib import quote

def attack(query, cmd):
    end_token = query.find('&')
    token = query[:end_token].split('=')[1]
    params = query[end_token+1:]

    pad_bytes = padding((8 + len(params)) * 8)

    kms = md5(state=token.decode('hex'), count=512) # set start state to end of user string
    kms.update(cmd)
    hashed = kms.hexdigest()
    print(hashed)

    return "token=" + hashed + "&" + params + quote(pad_bytes) + cmd


with open(sys.argv[1], 'r') as fuck:
    query_string = fuck.read().strip()

with open(sys.argv[2], 'r') as shit:
    kys = shit.read().strip()
    result = attack(query_string, kys)

with io.FileIO(sys.argv[3], 'w') as output:
    output.write(result)

