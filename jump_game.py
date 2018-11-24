'''
Problem: https://leetcode.com/problems/jump-game/
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lasPos = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if(i + nums[i] >= lasPos):
                lasPos = i
                
        return lasPos == 0
