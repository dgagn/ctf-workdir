from tqdm import *
import exrex

words = list(exrex.generate('^m4try0shk4#[A-Za-z]{2}[0-9]{4}$'))

with open('dict.txt', 'w') as f:
    for word in tqdm(words, total=len(words), unit="word"):
        f.write(word + '\n')
print("[!] Done")
