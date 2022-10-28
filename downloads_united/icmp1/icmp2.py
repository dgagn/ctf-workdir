from scapy.all import *
from pwn import *
from textwrap import wrap

ps = rdpcap("i-see-em-pee-2.pcapng")

with open('pee', 'wb') as file:
    for p in ps:
        file.write(p.load)
