'''
Problem: https://leetcode.com/problems/minimum-path-sum/
'''

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        dp = [[grid[i][j] for j in range(n)] for i in range(m)]
        
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                    
        return dp[m-1][n-1]
