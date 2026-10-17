# Problem: Collections.Counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

x = int(input())
shoe_sizes = Counter(map(int, input().split()))
n = int(input())

earnings = 0

for i in range(n):
    size, price = map(int, input().split())

    if shoe_sizes[size] > 0:
        earnings += price
        shoe_sizes[size] -= 1

print(earnings)