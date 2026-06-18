class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            k = 0

            for p in piles:
                k += math.ceil(p/m)

            if k <= h:
                res = min(m, res)
            
            if k <= h:
                r = m - 1
            else:
                l = m + 1
        return res

