## LCA algorithm + segment tree

import sys
from collections import deque
from math import sqrt
input = sys.stdin.readline

def setNodeDFS():
    q = deque([[1, 0]])
    visit = set()

    while q:
        curr, par = q.popleft()
        visit.add(curr)

        parents[curr][0] = par
        depths[curr] = depths[par] + 1

        pow = 1
        while 2 ** pow <= depths[curr]:
            parents[curr][pow] = parents[parents[curr][pow - 1]][pow - 1]
            pow += 1

        for child in edges[curr]:
            if child not in visit:
                q.append([child, curr])

    return

def climb(node, diff):
    n = len(parents[0]) - 1
    bitmask = 1 << n

    for _ in range(len(parents[0])):
        if diff & bitmask:
            node = parents[node][n]
        n -= 1
        bitmask >>= 1

    return node

def lca(node_1, node_2):
    i, j = min(node_1, node_2), max(node_1, node_2)
    if (i, j) in results:
        return results[(i, j)]

    if depths[node_1] > depths[node_2]:
        node_1 = climb(node_1, depths[node_1] - depths[node_2])
    elif depths[node_1] < depths[node_2]:
        node_2 = climb(node_2, depths[node_2] - depths[node_1])

    k, l = node_1, node_2
    if (k, l) in results:
        return results[(k, l)]

    if node_1 == node_2:
        results[(i, j)] = node_1
        return node_1
    else:
        answer = 1
        lo, hi = 1, depths[node_1]
        mid = (lo + hi) // 2

        while lo <= hi:
            runner_1 = climb(node_1, mid)
            runner_2 = climb(node_2, mid)

            if runner_1 != runner_2: # still doesn't match
                # so we can climb more
                node_1 = runner_1
                node_2 = runner_2
                hi = depths[node_1] - depths[answer]
            elif runner_1 == runner_2:
                # maybe we've already passed (or not), so should check more
                answer = runner_1
                hi = mid - 1
                
            mid = (lo + hi) // 2

        results[(i, j)] = answer
        results[(k, l)] = answer
        return answer

edge_num = int(sys.stdin.readline().rstrip())

edges = [[] for _ in range(edge_num + 1)]
parents = [[None for _ in range(int(sqrt(edge_num)))] for i in range(edge_num + 1)]
depths = [-1] + [0 for _ in range(edge_num)]
results = {}

for _ in range(edge_num - 1):
    node_1, node_2 = map(int, input().split())
    edges[node_1].append(node_2)
    edges[node_2].append(node_1)
    
setNodeDFS()

question_len = int(input())
for _ in range(question_len):
    node_1, node_2 = map(int, input().split())
    print(lca(node_1, node_2))