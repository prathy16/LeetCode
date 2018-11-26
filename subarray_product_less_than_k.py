'''
Problem: https://leetcode.com/problems/subarray-product-less-than-k/
'''

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if(k <= 1): return 0
        
        left = 0
        prod, ans = 1, 0
        
        for right, val in enumerate(nums):
            prod *= val
            
            while prod >= k:
                prod /= nums[left]
                left += 1
            '''
            number of contiguous subarrays that can be formed from left to right index 
            including the right item is right - left + 1
            '''   
            ans += right - left + 1
            
        return ans
