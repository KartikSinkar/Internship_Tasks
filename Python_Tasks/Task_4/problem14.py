# Problem: Set .add()
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
stamps = set()

for i in range(n):
    stamps.add(input().strip())

print(len(stamps))