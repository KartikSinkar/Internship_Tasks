# Problem: Symmetric Difference
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == '__main__':
    M = int(input())
    set_m = set(map(int, input().split()))
    N = int(input())
    set_n = set(map(int, input().split()))

    result = sorted(set_m.symmetric_difference(set_n))
    for number in result:
        print(number)
