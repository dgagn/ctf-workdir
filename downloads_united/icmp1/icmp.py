from scapy.all import *
from pwn import *

ps = rdpcap("i-see-em-pee-1.pcapng")

for p in ps:
    ch = chr(p.ttl)
    if ch != '<':
        print(ch, end="")
