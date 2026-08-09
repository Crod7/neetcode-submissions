class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 0

        while l < len(prices) and r < len(prices):
            if prices[r] > prices[l]:
                profit += (prices[r] - prices[l])
                l = r
            elif prices[r] < prices[l]:
                l += 1
            
            r += 1

        return profit
            