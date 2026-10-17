# Problem: The Minion Game
# HackerRank Link: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    stuart = 0
    kevin = 0
    vowels = "AEIOU"

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
