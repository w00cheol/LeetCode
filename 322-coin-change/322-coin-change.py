class Solution:
    def coinChange(self, coins: List[int], amount: int, cnt=0) -> int:
        dp = [0] + [amount+1 for _ in range(amount)]
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        if dp[amount] == amount+1: return -1
        return dp[amount]