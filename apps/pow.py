#!/usr/bin/env python

import hashlib
import sys

max_nonce = 2 ** 32 - 1 #max unsigned int_32

def proof_of_work(header, difficulty):
    target =  (0xffff * 2**208) / difficulty
    for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(header)+str(nonce)).hexdigest()
        # check if this is a valid result, below the target
        if long(hash_result, 16) < target:
            return nonce
    return None


if __name__ == '__main__':
    if len(sys.argv) == 3:
        header = sys.argv[1]
        difficulty = int(sys.argv[2])
        print proof_of_work(header, difficulty)
