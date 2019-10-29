#!/usr/bin/python

import sys
from strip_accents import text_to_id
import hashlib


def generate_GUID(keyInput):

    key = keyInput
    keygood = text_to_id(key)
    GUID = hashlib.sha256(keygood.encode('utf-8')).hexdigest()
    return GUID


if len(sys.argv) > 1:

    if len(sys.argv) == 5:
        key = sys.argv[1]+sys.argv[2]+sys.argv[3]+sys.argv[4]
        print(generate_GUID(key))

    if len(sys.argv) == 2:
        key = sys.argv[1]
        print(generate_GUID(key))

    else:
        print("mauvais nombre d'arguments")