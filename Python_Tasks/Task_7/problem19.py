# Weighted Uniform Strings
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def weightedUniformStrings(s, queries):
    weights = set()
    previous_char = ''
    run_length = 0

    for char in s:
        if char == previous_char:
            run_length += 1
        else:
            previous_char = char
            run_length = 1

        weights.add((ord(char) - ord('a') + 1) * run_length)

    return ["Yes" if query in weights else "No" for query in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()