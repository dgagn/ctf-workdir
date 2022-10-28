from pwn import *

print(
    shellcraft.pushstr('/bin/cat /challenge/banner.txt')
)

print(
    shellcraft.pushstr('/bin/sh')
)
