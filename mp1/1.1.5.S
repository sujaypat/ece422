.global _main
.section .text

_main:

push	%ebp
mov	%esp, %ebp

xorl	%eax, %eax
pushl	%eax

pushl	$0x68732f2f
pushl	$0x6e69622f

movl	%esp, %ebx
movl	%eax, %ecx
movl	%eax, %edx

movb	$0xb, %al
int	$0x80

leave
ret
