class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        hashset = set()

        maxSize = 0

        for i, c in enumerate(s):

            while c in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(c)
            r += 1

            if (r - l) > maxSize:
                maxSize = (r - l)
                
        return maxSize

            
