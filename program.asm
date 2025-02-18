%DEFINE SYS_WRITE 1
%DEFINE STDOUT 1
%DEFINE SYS_EXIT 60

section .rodata
hello:
    .msg db 'Hello World!', 0xA
    .len equ $- .msg
section .text

global _start

_start:
    MOV RAX, SYS_WRITE
    MOV RDI, STDOUT
    MOV RSI, hello.msg
    MOV RDX, hello.len
    SYSCALL

    MOV RAX, SYS_EXIT
    XOR RDI, RDI
    SYSCALL