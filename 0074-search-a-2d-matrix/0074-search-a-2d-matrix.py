class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])  
        low, high = 0, (n * m) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_row = mid // m
            mid_col = mid % m
            mid_val = matrix[mid_row][mid_col]  

            if mid_val == target:
                return True

            if mid_val < target:
                low = mid + 1
            elif mid_val > target:
                high = mid - 1

        return False