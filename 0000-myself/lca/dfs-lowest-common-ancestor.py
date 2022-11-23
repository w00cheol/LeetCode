import sys
input = sys.stdin.readline

def lca(curr=1):
    visit.add(curr)
    found_cnt = 0

    if curr == node_1 or curr == node_2:
        found_cnt += 1

    for child in edges[curr]:
        if child not in visit:
            child_lca = lca(child)
                
            if child_lca[0] == 2: # child has already found LCA! return it
                return child_lca

            if child_lca[0] == 1: # one of its children has one node
                found_cnt += 1 # so found_cnt ++

                if found_cnt == 2:
                    # we found (1 child + curr) or (2 children)
                    # ,which means current node is LCA
                    return [2, curr]

    return [found_cnt, curr]
    

edge_num = int(sys.stdin.readline().rstrip())
edges = [[] for _ in range(edge_num + 1)]

for _ in range(edge_num - 1):
    node_1, node_2 = map(int, input().split())
    edges[node_1].append(node_2)
    edges[node_2].append(node_1)
    
question_len = int(input())
for _ in range(question_len):
    node_1, node_2 = map(int, input().split())

    if node_1 == node_2:
        print(node_2)
    else:
        visit = set()
        print(lca()[-1])