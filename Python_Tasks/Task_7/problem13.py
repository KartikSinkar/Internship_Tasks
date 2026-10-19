# Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def isValid(s):
    frequencies = Counter(Counter(s).values())

    if len(frequencies) == 1:
        return "YES"
    if len(frequencies) != 2:
        return "NO"
    (freq1, count1), (freq2, count2) = frequencies.items()
    if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
        return "YES"
    if abs(freq1 - freq2) == 1 and (count1 == 1 or count2 == 1):
        return "YES"
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
