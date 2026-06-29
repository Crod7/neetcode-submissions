class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m1 = 0
        m2 = 0
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m1 = (l + r) // 2

            if matrix[m1][0] > target:
                r = m1 - 1
            elif matrix[m1][-1] < target:
                l = m1 + 1
            else:
                if matrix[m1][0] == target:
                    return True
                break
        
        l = 0
        r = len(matrix[m1]) - 1

        while l <= r:
            m2 = (l + r) // 2
            if target > matrix[m1][m2]:
                l = m2 + 1
            elif target < matrix[m1][m2]:
                r = m2 - 1
            else:
                return True
                
        return False




