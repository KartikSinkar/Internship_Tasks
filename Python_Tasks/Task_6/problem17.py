# Problem: Check Strict Superset
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

set_a = set(map(int, input().split()))
number_of_sets = int(input())

is_strict_superset = True

for _ in range(number_of_sets):
    other_set = set(map(int, input().split()))

    if not (set_a > other_set):
        is_strict_superset = False
        break

print(is_strict_superset)
