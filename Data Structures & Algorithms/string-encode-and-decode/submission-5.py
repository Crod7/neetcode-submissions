class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if strs == []:
            return "--;;--"

        for s in strs:
            res = res + s + ";;"
        
        return res[:-2]

    def decode(self, s: str) -> List[str]:
        if s == "--;;--":
            return[]
        return s.split(";;")
