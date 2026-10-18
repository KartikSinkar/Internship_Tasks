# Problem: Set .difference() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

print(len(english.difference(french)))
