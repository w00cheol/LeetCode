class Solution:
    def dfs(self, node, visited):
        if not node: return node
        new_node = Node(node.val)
        visited[new_node.val] = new_node
        for old_neighbor in node.neighbors:
            if old_neighbor.val in visited:
                new_node.neighbors.append(visited[old_neighbor.val])
            else:
                new_node.neighbors.append(self.dfs(old_neighbor, visited))
        return new_node
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.dfs(node, {})