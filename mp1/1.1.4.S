.global your_asm_fn
.section .text

your_asm_fn:

push	%ebp
mov	%esp,%ebp
push	%ebx

push	$0x646f6f66
push	$0x6c6f6f63
mov	%esp, %eax

push	$0xc105ed
mov	%esp, %ebx

push	%eax
push	%ebx
push	$0xacce55ed

call practice

pop	%ebx
pop	%ebx
pop	%ebx
pop	%ebx
pop	%ebx

leave
ret
