class Solution:
    def change(self, amount: int, coins):
        answer = [1] + [0] * amount # the answer of index that indicates the number of amount
        
        for coin in coins:
            for i in range(coin, amount + 1):
                answer[i] += answer[i - coin]
                        
        return answer[amount]