#!/usr/bin/python3

import string
import random

def passgen (size=6, chars=string.ascii_lowercase+string.digits):
	return ''.join (random.choice(chars) for _ in range(size))


if __name__ in '__main__':
	print ( passgen() )
