class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer, x, y = 0, 0, len(height)-1
        while x != y:
            if height[x] > height[y]:
                answer = max(answer, height[y] * (y-x))
                y -= 1
            else:
                answer = max(answer, height[x] * (y-x))
                x += 1
        return answer