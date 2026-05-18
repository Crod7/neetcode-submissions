class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxh = 0
        while l < r:
            # replace maxh if is new highest value
            if heights[l] < heights[r]:
                temp = heights[l] * (r-l)
                if temp > maxh:
                    maxh = temp
            else:
                temp = heights[r] * (r-l)
                if temp > maxh:
                    maxh = temp
            
            # determine where to move pointer
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return maxh

