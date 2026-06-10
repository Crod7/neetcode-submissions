class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        m = 0

        while l <= r:
            m = l + ((r-l)//2)
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] < target:
                l = m + 1
            elif matrix[m][0] == target:
                return True
            if target > matrix[m][0]:
                # last array, check this one
                if m == len(matrix) - 1:
                    break
                # verify if target is smaller than next array
                if target < matrix[m + 1][0]:
                    break

        n = m
        print(matrix[n])
        l, r = 0, len(matrix[n]) - 1

        while l <= r:
            m = l + ((r-l)//2)
            if matrix[n][m] > target:
                r = m - 1
            elif matrix[n][m] < target:
                l = m + 1
            else:
                return True
        return False