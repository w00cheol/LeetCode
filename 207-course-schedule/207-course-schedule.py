from collections import defaultdict

class Solution:
    def dfs(self, i, dic, visited):
        if i in visited:
            return False
        visited.append(i)
        for j in dic[i]:
            if self.dfs(j, dic, visited[::]) == False:
                return False
        dic[i] = []
        return True
                
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        for i in range(len(prerequisites)):
            dic[prerequisites[i][0]].append(prerequisites[i][1])
        for i in range(numCourses):
            if self.dfs(i, dic, []) == False:
                return False
        return True