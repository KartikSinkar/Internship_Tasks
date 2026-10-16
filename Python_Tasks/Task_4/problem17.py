# Problem: Finding the Percentage
# HackerRank Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    students = {}

    for _ in range(n):
        data = input().split()
        name = data[0]
        marks = list(map(float, data[1:]))
        students[name] = marks

    query_name = input()
    average = sum(students[query_name]) / len(students[query_name])

    print("{:.2f}".format(average))