class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
   
        
        l = 1
        r = max(piles)
        result = r

        while l <= r:
            m = (l + r) //2
            currHours = 0

            for p in piles:
                currHours += math.ceil(p / m)

            if currHours <= h:
                result = m
                r = m - 1
            
            if currHours > h:
                l = m + 1  
        return result

            
