class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2

            currHours = 0
            for p in piles:
                currHours += math.ceil(p/m)
            
            if currHours <= h and m != 0:
                res = min(m, res)
                r = m - 1
            else:
                l = m + 1

        return res
                