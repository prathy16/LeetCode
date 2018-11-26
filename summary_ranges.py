'''
Problem: https://leetcode.com/problems/summary-ranges/
'''

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if(nums == []): 
            return []
        
        nums.append(9999999)
        
        ret_list = []
        prev = nums[0]
        
        for i in range(1, len(nums)):
            if(nums[i] != nums[i-1] + 1):
                if(prev == nums[i-1]):
                    ret_list.append(str(prev))
                else:
                    ret_list.append(str(prev) + '->' + str(nums[i-1]))
                    
                prev = nums[i]
                
        return ret_list
