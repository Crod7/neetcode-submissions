class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        m1 = 0
        m2 = 0
        while l <= r:
            m1 = (l + r) // 2

            if matrix[m1][0] < target and matrix[m1][-1] > target:
                #
                break
            elif matrix[m1][-1] < target:
                #
                l = m1 + 1
            elif matrix[m1][0] > target:
                r = m1 - 1
            else:
                return True
        print(matrix[m1])

        l, r = 0, len(matrix[m1]) - 1
        while l <= r:
            m2 = (l + r) // 2

            if matrix[m1][m2] > target:
                #
                r = m2 - 1
            elif matrix[m1][m2] < target:
                #
                l = m2 + 1
            else:
                return True
        return False


