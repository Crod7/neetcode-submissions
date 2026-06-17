class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)
        res = 0

        while l <= r:
            m = (l + r) // 2

            currHours = 0
            for p in piles:
                if m != 0:
                    currHours += math.ceil(p/m)
            
            if currHours <= h and m != 0:
                # init res being set
                if res == 0:
                    res = m
                else:
                    res = min(m, res)
                r = m - 1
            else:
                l = m + 1

        return res
                