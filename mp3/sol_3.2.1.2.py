import sys, io
from pymd5 import md5, padding
from urllib import quote

def attack(query, cmd):
    idx = query.find('&')
    token = query[:idx].split('=')[1]

    cmds = query[idx+1:]

    pad = padding((8 + len(cmds)) * 8)

    before = md5(state=token.decode('hex'), count=512)
    before.update(cmd)
    hashed = before.hexdigest()
    print(hashed)

    return "token=" + hashed + "&" + cmds + quote(pad) + cmd


with open(sys.argv[1], 'r') as f1:
    q = f1.read().strip()

with open(sys.argv[2], 'r') as f2:
    cmd = f2.read().strip()
    res = attack(q, cmd)

with io.FileIO(sys.argv[3], "w") as out:
    out.write(res)

