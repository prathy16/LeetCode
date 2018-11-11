'''
Problem: https://leetcode.com/problems/count-numbers-with-unique-digits/
'''

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 0): return 1
        if(n == 1): return 10
        
        dp = [0 for _ in range(n+1)]
        
        dp[1], dp[2] = 10, 81
        
        for i in range(3, n+1):
            dp[i] = dp[i-1]*(11-i)
            
        return sum(dp)
