import sys
from collections import deque

person_cnt, clue_cnt = map(int, sys.stdin.readline().split())

ranks = [0] * (person_cnt + 1)
clues = [[] for _ in range(person_cnt + 1)]

for _ in range(clue_cnt):
    winner, loser = map(int, sys.stdin.readline().split())
    clues[winner].append(loser)
    ranks[loser] += 1

q = deque()
for i in range(1, len(ranks)):
    if ranks[i] == 0:
        q.append(i)

while q:
    person_idx = q.popleft()
    print(person_idx)

    for loser in clues[person_idx]:
        ranks[loser] -= 1
        if ranks[loser] == 0:
            q.append(loser)