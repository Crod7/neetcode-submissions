class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        if strs == []:
            return "--;;--"

        for s in strs:
            result = result + s + ":;:"
        return result[:-3]

    def decode(self, s: str) -> List[str]:
        if s == "--;;--":
            return []

        result = s.split(":;:")
        return result