class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashsetS = {}
        hashsetT = {}

        for n in s:
            hashsetS[n] = 1 + hashsetS.get(n, 0)
        for n in t:
            hashsetT[n] = 1 + hashsetT.get(n, 0)
        
        if hashsetS == hashsetT:
            return True
        else:
            return False
    
