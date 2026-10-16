# Problem: Find the Runner-Up Score!
# HackerRank Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    unique_scores = sorted(set(scores))
    print(unique_scores[-2])
