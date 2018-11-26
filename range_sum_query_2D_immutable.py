'''
Problem: https://leetcode.com/problems/range-sum-query-2d-immutable/
'''


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                self.dp[i+1][j+1] = self.dp[i+1][j] + self.dp[i][j+1] + matrix[i][j] - self.dp[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
