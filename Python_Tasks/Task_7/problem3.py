# Mars Exploration
# https://www.hackerrank.com/challenges/mars-exploration/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def marsExploration(s):
    expected = "SOS"
    changes = 0

    for i, char in enumerate(s):
        if char != expected[i % 3]:
            changes += 1

    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
