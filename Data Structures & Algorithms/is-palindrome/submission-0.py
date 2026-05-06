class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned = cleaned + c.lower()
        rev = cleaned[::-1]
        if cleaned == rev:
            return True
        else:
            return False
