class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l,r = 0,0
        maxProfit = 0
        profit = 0

        if len(prices) == 1:
            return 0

        for i, p in enumerate(prices):
            if i == 0:
                continue

            if p < prices[l]:
                l, r = i, i
            if p > prices[r]:
                r = i

            profit = prices[r] - prices[l]
            if profit > maxProfit:
                maxProfit = profit


            

        return maxProfit
