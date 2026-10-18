# Problem: Check Subset
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-subset/problem

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    set_a = set(map(int, input().split()))

    m = int(input())
    set_b = set(map(int, input().split()))

    print(set_a.issubset(set_b))
