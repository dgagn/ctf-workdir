from Crypto.Util.number import long_to_bytes

N = 0xac586f447e16c51821999902cf993f47
e = 0x10001
cipher = 0x9b7a8eb8ad559e3f52ff3ceeaf0025a4
# factor with cado-nfs
p, q = 172036442175296373253148927105725488217, 337117592532677714973555912658569668821

assert p * q == N

p_roots = mod(cipher, p).nth_root(e, all=True)
q_roots = mod(cipher, q).nth_root(e, all=True)

for xp in p_roots:
    for xq in q_roots:
        x = crt([Integer(xp), Integer(xq)], [p,q])
        x = int(x)
        flag = long_to_bytes(x)
        if flag.startswith(b"dice"):
            print(flag.decode())