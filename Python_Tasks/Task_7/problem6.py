# Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def pangrams(s):
    letters = set(char.lower() for char in s if char.isalpha())
    return "pangram" if len(letters) == 26 else "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
