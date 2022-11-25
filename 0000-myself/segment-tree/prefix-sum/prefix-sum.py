import sys
from math import log2

def initSegTree(idx, start, end):
    if start == end:
        seg_tree[idx] = nums[start]
    else:
        mid = (start + end) // 2
        seg_tree[idx] = initSegTree(2*idx, start, mid) + initSegTree(2*idx + 1, mid + 1, end)
    
    return seg_tree[idx]

# idx (node's index number)
# start ~ end (range that this node has prefix sum of)
# left ~ right (range that we have to find)
def prefixSum(idx, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return seg_tree[idx]

    mid = (start + end) // 2
    return prefixSum(idx*2, start, mid, left, right) + prefixSum(idx*2 + 1, mid + 1, end, right)


nums = []
nums_len = int(sys.stdin.readline().rstrip())
for _ in range(nums_len):
    nums.append(int(sys.stdin.readline().rstrip()))

if nums_len == 1:
    depth_max = 1
else:
    depth_max = int(log2(2 * nums_len - 1)) + 1

seg_tree = [None] * (2 ** depth_max)

initSegTree(1, 0, nums_len - 1)