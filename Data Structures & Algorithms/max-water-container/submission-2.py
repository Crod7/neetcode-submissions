class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 0
        l, r = 0, len(heights) - 1

        while l < r:
            maxl, maxr = heights[l], heights[r]

            if maxl < maxr:
                temp = (r - l) * maxl
                l += 1
            else:
                temp = (r - l) * maxr
                r -= 1
            
            if temp > currMax:
                currMax = temp
            
        
        return currMax
