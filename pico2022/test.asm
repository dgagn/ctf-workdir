section .text
    global _start

_start:
    xor eax, eax
    push eax
    push 0x0A646c72 ; hello world
    push 0x6f77206f
    push 0x6c6c6548
    mov bl, 0x1 ; stdout
    mov ecx, esp ; the address of hello world
    mov dl, 0xe ; the length of hello world
    mov al, 0x4  ; sys_write syscall
    int 0x80 ; call the syscall
    mov al, 0x1 ; sys_exit syscall
    int 0x80 ; call the syscall