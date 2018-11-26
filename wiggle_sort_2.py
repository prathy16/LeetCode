'''
Problem: https://leetcode.com/problems/wiggle-sort/
'''

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # stefanPochmann's solution
        
        # Sort the numbers
        nums.sort()
        
        # number of even places in the list
        half = len(nums[::2])
        
        """
        first half of the numbers will be placed at the even indices in the reverse order
        second half of the numbers will be placed at the odd indices in the reverse order
        """
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
                
                
