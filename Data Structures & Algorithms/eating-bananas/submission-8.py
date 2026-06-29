class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        k = r
        res = r

        while l <= r:
            m = (l + r) // 2
            tempH = 0
            for p in piles:
                tempH += math.ceil(p / m)

            if tempH <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        
        return res


   
        

            
