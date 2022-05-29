class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        m = M = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < m:
                answer = max(answer, M - m)
                m = M = prices[i]
            elif prices[i] > M:
                M = prices[i]
        return max(answer, M - m)
        