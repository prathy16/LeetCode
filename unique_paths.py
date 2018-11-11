'''
Problem: https://leetcode.com/problems/unique-paths/
'''

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if(i - 1 < 0 and j - 1 < 0):
                    dp[i][j] = 1
                elif(i - 1 < 0):
                    dp[i][j] = dp[i][j-1]
                elif(j - 1 < 0):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    
        return dp[m-1][n-1]
