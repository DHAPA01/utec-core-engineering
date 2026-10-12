#!/usr/bin/env python3
alphabet = ""
for code in range(97, 123):
    if code != 101 and code != 113:
        alphabet += chr(code)
print("{}".format(alphabet))
