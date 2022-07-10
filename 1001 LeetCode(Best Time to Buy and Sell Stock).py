# Brute force algorithm

class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        return max_profit
