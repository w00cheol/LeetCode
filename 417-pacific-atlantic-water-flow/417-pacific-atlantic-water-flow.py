class Solution:
    heights, dxy = [], [[-1, 0], [1, 0], [0, -1], [0, 1]]
    def dfs(self, i, j, visited):
        if (i, j) in visited:
            return
        visited.add((i, j))
        for d in self.dxy:
            moved_i, moved_j = i+d[0], j+d[1]
            if 0 <= moved_i < len(self.heights) and 0 <= moved_j < len(self.heights[0]):
                if self.heights[i][j] <= self.heights[moved_i][moved_j]:
                    self.dfs(moved_i, moved_j, visited) # until maximum heights from start point
                    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        row, col = len(heights), len(heights[0])
        p_area, a_area = set(), set()
        
        # O(n)
        for i in range(row):
            self.dfs(i, 0, p_area)
            self.dfs(i, col-1, a_area)
        # O(n)
        for i in range(col):
            self.dfs(0, i, p_area)
            self.dfs(row-1, i, a_area)

        return p_area & a_area