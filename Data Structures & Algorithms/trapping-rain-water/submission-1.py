class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i, h in enumerate(height):
            l, r = i, i
            maxl = 0
            maxr = 0

            while l >= 0:
                if height[l] > maxl:
                    maxl = height[l]
                l -= 1
            while r <= len(height) - 1:
                if height[r] > maxr:
                    maxr = height[r]
                r += 1
            
            if maxl < maxr:
                temp = maxl - h
                if temp > 0:
                    water += temp
            else:
                temp = maxr - h
                if temp > 0:
                    water += temp
        return water
