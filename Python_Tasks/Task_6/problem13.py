# Problem: Set .union() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-union/problem

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

print(len(english.union(french)))
