import itertools
import string
import collections
from hashlib import sha256

flag = 'QRXD-UUUXGIL4DVZP'
key = 'lgxx'

lowercase = collections.deque(string.ascii_lowercase + string.digits)

def encrypt(message, key, multiplier = -1):
    compressed_message = message.lower()

    cycler = itertools.cycle(key.lower())
    long_key = ''.join([cycler.__next__() for _ in range(len(compressed_message))])

    coded = []
    for number in range(len(long_key)):
        try:
            cipher_letter = compressed_message[number]
            key_letter = long_key[number]
            key_index = string.ascii_lowercase.index(key_letter)
            cipher_index = string.ascii_lowercase.index(cipher_letter)

            lowercase = collections.deque(string.ascii_lowercase)
            lowercase.rotate(multiplier * key_index)
            new_alphabet = ''.join(list(lowercase))
            new_char = new_alphabet[cipher_index]
            coded.append(new_char)
        except:
            coded.append(compressed_message[number])

    return ''.join(coded)


def decrypt(message, key):
    return encrypt(message, key, 1)

print(decrypt(flag, key))