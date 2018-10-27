'''
Problem: https://leetcode.com/problems/single-number-ii/
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (3*(sum(set(nums))) - sum(nums))//2
