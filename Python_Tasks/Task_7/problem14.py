# Anagram
# https://www.hackerrank.com/challenges/anagram/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    mid = len(s) // 2
    first = Counter(s[:mid])
    second = Counter(s[mid:])

    return sum((first - second).values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
