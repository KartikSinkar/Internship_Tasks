# Problem: Word Order
# HackerRank Link: https://www.hackerrank.com/challenges/word-order/problem

n = int(input())
word_counts = {}

for i in range(n):
    word = input()

    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(len(word_counts))

for count in word_counts.values():
    print(count, end=" ")

