# Problem: Find the Runner-Up Score!
# HackerRank Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = sorted(set(arr))
    print(scores[-2])
