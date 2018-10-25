'''
Problem: https://leetcode.com/problems/contains-duplicate-ii/
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        duplicateSet = set()
        
        # maintain a window of size k and duplicate is found return True
        for i in range(len(nums)):
            if nums[i] in duplicateSet: return True
            duplicateSet.add(nums[i])
            if(len(duplicateSet) > k):
                duplicateSet.discard(nums[i-k])
        # If no duplicate found       
        return False
