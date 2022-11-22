import sys
from collections import deque
input = sys.stdin.readline

def setNodeDFS():
    q = deque([[1, 0]])
    visit = set()

    while q:
        curr, par = q.popleft()
        visit.add(curr)

        parents[curr] = par
        depths[curr] = depths[par] + 1

        for child in edges[curr]:
            if child not in visit:
                q.append([child, curr])

    return

def lca(node_1, node_2):
    if depths[node_1] > depths[node_2]:
        for _ in range(depths[node_1] - depths[node_2]):
            node_1 = parents[node_1]
    elif depths[node_1] < depths[node_2]:
        for _ in range(depths[node_2] - depths[node_1]):
            node_2 = parents[node_2]
            
    while node_1 != node_2:
        node_1 = parents[node_1]
        node_2 = parents[node_2]

    return node_1

edge_num = int(sys.stdin.readline().rstrip())

edges = [[] for _ in range(edge_num + 1)]
parents = [[] for _ in range(edge_num + 1)]
depths = [0] + [[] for _ in range(edge_num)]

for _ in range(edge_num - 1):
    node_1, node_2 = map(int, input().split())
    edges[node_1].append(node_2)
    edges[node_2].append(node_1)
    
setNodeDFS()

question_len = int(input())
for _ in range(question_len):
    node_1, node_2 = map(int, input().split())
    print(lca(node_1, node_2))