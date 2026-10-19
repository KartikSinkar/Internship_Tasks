# Game of Thrones - I
# https://www.hackerrank.com/challenges/game-of-thrones/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def gameOfThrones(s):
    odd_counts = sum(1 for count in Counter(s).values() if count % 2 != 0)
    return "YES" if odd_counts <= 1 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
