from pwn import *
from zipfile import *
from tqdm import *

info('loading dictionary in memory')
p = process([''])