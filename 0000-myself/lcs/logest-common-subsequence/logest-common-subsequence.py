import sys
a = str(sys.stdin.readline().rstrip())
b = str(sys.stdin.readline().rstrip())

answers = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

for r in range(1, len(answers)):
    for c in range(1, len(answers[0])):
        answers[r][c] = max(answers[r-1][c], answers[r][c-1], answers[r-1][c-1] + (a[r-1] == b[c-1]))

print(answers[-1][-1])