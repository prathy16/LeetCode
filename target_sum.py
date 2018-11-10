'''
Problem: https://leetcode.com/problems/target-sum
'''

class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        from collections import defaultdict
        if not nums:
            return 0
        
        dict_sum = defaultdict(int)
        if(nums[0] == 0):
            dict_sum[nums[0]] = 2
        else:
            dict_sum[nums[0]], dict_sum[-nums[0]] = 1, 1
        
        for num in nums[1:]:
            temp = defaultdict(int)
            for s, v in dict_sum.items():
                temp[s+num] += v
                temp[s-num] += v
                
            dict_sum = temp
                
        return dict_sum[S]
