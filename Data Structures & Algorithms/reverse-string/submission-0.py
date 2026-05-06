class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        while i < len(s):
            tempA = s[i]
            tempB = s[-1 - i]

            if i >= len(s) - i:
                break

            s[i] = tempB
            s[-1 - i] = tempA

            i = i + 1
        
        