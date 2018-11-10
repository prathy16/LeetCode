'''
Problem: https://leetcode.com/problems/maximum-product-subarray
'''

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod = nums[0]
        _max, _min = max_prod, max_prod
        
        for num in nums[1:]:
            if num < 0:
                _max, _min = _min, _max
                
            _max = max(num, num*_max)
            _min = min(num, num*_min)
            
            max_prod = max(max_prod, _max)
            
        return max_prod
                
