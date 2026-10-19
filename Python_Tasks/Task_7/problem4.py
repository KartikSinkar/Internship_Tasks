# Funny String
# https://www.hackerrank.com/challenges/funny-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def funnyString(s):
    values = [ord(char) for char in s]
    forward = [abs(values[i] - values[i - 1]) for i in range(1, len(values))]
    reverse = forward[::-1]

    return "Funny" if forward == reverse else "Not Funny"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
