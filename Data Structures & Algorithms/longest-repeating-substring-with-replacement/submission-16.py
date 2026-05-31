class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxResult = 0
        for i in range(len(s)):
            l = i
            r = i
            count = 0
            hashmap = {}
            while r < len(s):
                hashmap[s[r]] = 1 + hashmap.get(s[r], 0)

                mostFreqChar = max(hashmap, key=hashmap.get)
                

                if len(s[l:r]) - hashmap[mostFreqChar] > k:
                    hashmap[s[l]] -= 1
                    hashmap[s[r]] -= 1
                    l += 1
                else:
                    r += 1


                if len(s[l:r]) - hashmap[mostFreqChar] <= k:
                    maxResult = max(maxResult, len(s[l:r]))
        return maxResult
            

