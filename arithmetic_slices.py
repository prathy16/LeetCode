'''
Problem: https://leetcode.com/problems/arithmetic-slices/
'''
class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp, arithmetic_sum = 0, 0
        
        for i in range(2, len(A)):
            if(A[i]-A[i-1] == A[i-1]-A[i-2]):
                dp             = 1 + dp
                arithmetic_sum = arithmetic_sum + dp
            else:
                dp = 0
                
        return arithmetic_sum
