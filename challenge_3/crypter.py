#!/usr/bin/env python2

"""
THIS IS A COPY OF MY AWESOME CRYPTER.
NO TIME TO WRITE A DECRYPTER AT THIS MOMENT.
HAVE TO MAKE SURE I WRITE DOWN THE TIMESTAMPS!!!
"""

import sys
import os
import string

def generate_key():
    enc_key = []
    raw_key = os.popen("date +%s").read().strip()
    for d in xrange(0, len(raw_key), 2):
        enc_key.append(raw_key[d:d+2])
    return enc_key

def encrypt(plain_msg):
    enc_msg = []
    enc_key = generate_key()
    for c in plain_msg:
        for e in enc_key:
            buf = "." + str(ord(c) ^ int(e))
            enc_msg.append(buf)
    return ''.join(enc_msg)

def decrypt(enc_key, enc_msg):
    plain_msg = ""
    return "NOT READY YET"