class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        finalResult = []

        l = 0
        r = 0

        def dfs(subset, l, r):
            if l == n and r == n:
                result.append(subset.copy())
                return

            if l <= r:
                subset.append("(")
                l += 1
                dfs(subset.copy(), l, r)
            else: # normal ( or )
                if l < n:
                    subset.append("(")
                    l += 1
                    dfs(subset.copy(), l, r)
                    subset.pop()
                    l -=1
                if r < n:
                    #subset.pop()

                    subset.append(")")
                    r += 1
                    dfs(subset.copy(), l, r)

        dfs([], 0, 0)

        for p in result:
            temp = "".join(p)
            finalResult.append(temp)

        return finalResult