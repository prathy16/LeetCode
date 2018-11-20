'''
Problem: https://leetcode.com/problems/3sum/
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = [] 
        
        for i in range(len(nums)):
            if(i != 0 and nums[i] == nums[i-1]): 
                continue
                
            target = nums[i] * -1
            s, e = i+1, len(nums) - 1
            
            while(s < e):
                if(nums[s] + nums[e] == target):
                    triplets.append([nums[i], nums[s], nums[e]])
                    s = s + 1
                    while(s < e and nums[s] == nums[s-1]):
                        s = s + 1
                    e = e - 1
                elif(nums[s] + nums[e] < target):
                    s = s + 1
                else:
                    e = e - 1
                    
        return triplets
                
                
