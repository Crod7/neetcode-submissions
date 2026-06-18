class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        m = 0

        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] <= target and matrix[m][-1] >= target:
                if m == target:
                    return True
                break
            elif matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
        
        l = 0
        r = len(matrix[m]) - 1
        while l <= r:
            z = (l + r) // 2

            if matrix[m][z] > target:
                r = z - 1
            elif matrix[m][z] < target:
                l = z + 1
            else:
                return True
        return False
