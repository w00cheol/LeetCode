class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        answer = [0] + [2e9 for _ in range(amount)]
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0 and answer[i - coin] != 2e9:
                    answer[i] = min(answer[i], 1 + answer[i - coin])
        return answer[-1] if answer[-1] != 2e9 else -1