# Problem: Company Logo
# HackerRank Link: https://www.hackerrank.com/challenges/most-commons/problem

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    counts = Counter(s)

    for character, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:3]:
        print(character, count)
