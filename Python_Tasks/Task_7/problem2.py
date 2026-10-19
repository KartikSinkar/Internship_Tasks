# The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
rooms = list(map(int, input().split()))

room_set = set(rooms)
captain_room = (sum(room_set) * k - sum(rooms)) // (k - 1)

print(captain_room)
