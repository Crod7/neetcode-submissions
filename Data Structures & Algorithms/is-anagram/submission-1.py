class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        if len(s) == 0:
            return True
        
        hashsetS = {}
        hashsetT = {}

        for c in s:
            hashsetS[c] = 1 + hashsetS.get(c, 0)

        for c in t:
            hashsetT[c] = 1 + hashsetT.get(c, 0)

        if hashsetS == hashsetT:
            return True
        return False