import base64
from pwn import *

# p = remote('nc.ctf.unitedctf.ca', 5003)
#
# with open('repo.zip', 'rb') as fin, open('repo.zip.b64', 'wb') as fout:
#     base64.encode(fin, fout)
#
# with open('repo.zip.b64', 'rb') as fin:
#     lines = fin.readlines()
#     lines = [line.rstrip() for line in lines]
#     for line in lines:
#         p.sendline(line)
#     p.sendline('EOF')
#     pprint(p.recv())

with open('anotherrepo.zip.b64', 'rb') as fin, open('output.zip', 'wb') as fout:
    base64.decode(fin, fout)

# info('interactive mode now')
# p.interactive()