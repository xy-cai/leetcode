class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        if not n:
            return False
        m = len(matrix[0])
        if not m:
            return False
        row = 0
        col = m-1
        while True:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1
            if col < 0 or row >= n:
                return False
        return False
        