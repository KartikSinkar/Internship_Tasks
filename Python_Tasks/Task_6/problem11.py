# Problem: String Formatting
# HackerRank Link: https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(n):

    width = len(format(n, "b"))

    for i in range(1, n + 1):
        print(
            str(i).rjust(width),
            format(i, "o").rjust(width),
            format(i, "X").rjust(width),
            format(i, "b").rjust(width)
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
