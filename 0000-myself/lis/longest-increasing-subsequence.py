from bisect import bisect_left
import sys
nums = map(int, list(sys.stdin.readline().rstrip().split()))

answer = [2e9]

for num in nums:
    order = bisect_left(answer, num)
    if order == len(answer):
        answer.append(num)
    else:
        answer[order] = num

print(len(answer))