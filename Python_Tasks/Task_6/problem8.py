# Problem: Tuples
# HackerRank Link: https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(raw_input()) # type: ignore
    integer_list = map(int, raw_input().split()) # type: ignore

    t = tuple(integer_list)
    print(hash(t))