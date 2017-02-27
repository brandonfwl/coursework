#!/usr/bin/python3.5
'''
Assignment 2
Brandon Fowler
CS131A
02-26-2017

'''

import sys

r_stage = sys.argv[::-1]

for i in range(len(r_stage)):
    if 'reverse.py' in r_stage[i]:
        pass
    else:
        print('Argument', i + 1, ' ', r_stage[i])
