from pwn import *

f = open("dict.csv", "r")
content = f.read().split('\n')
encrypted = b64d('XWxPUD5HSBhAR1gHVnh9b31mNUg=')

for word in content:
    encrypted = xor(encrypted, word)

print(encrypted)
