import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

answers = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]
max_answer = 0

for r in range(1, len(answers)):
    for c in range(1, len(answers[0])):
        answers[r][c] = answers[r-1][c-1] + (a[r] == b[c])
        max_answer = max(max_answer, answers[r][c])

print(max_answer)