class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0] * 26
        for c in s1:
            temp = ord(c) - ord('a')
            s1Count[temp] += 1

        s2Count = [0] * 26
        l, r = 0, 0
        while r < len(s2):
            temp = ord(s2[r]) - ord('a')
            if s2Count[temp] < s1Count[temp]:
                s2Count[temp] += 1
                r += 1
            else:
                temp = ord(s2[l]) - ord('a')
                s2Count[temp] -= 1
                l += 1
            
            if s1Count == s2Count:
                return True
        return False



