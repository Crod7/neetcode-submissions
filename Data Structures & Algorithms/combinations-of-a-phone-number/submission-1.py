class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        print(digits)
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(subset, i):
            # while i < len(digits) - 1 and digits[i] == digits[i + 1]:
            #     i += 1

            if i >= len(digits):

                valueItem = "".join(subset.copy())
                if valueItem != "":
                    result.append(valueItem)
                return

            chars = digitToChar[digits[i]]
        
            for char in chars:
                subset.append(char)
                dfs(subset, i + 1)
                subset.pop()
        
        dfs([], 0)

        return result