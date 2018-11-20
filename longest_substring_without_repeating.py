'''
Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        usedChar = {}
        longest, start = 0, 0
        
        for index, char in enumerate(s):
            if char in usedChar and start <= usedChar[char]:
                start = usedChar[char] + 1
            usedChar[char] = index
            longest = max(longest, index - start + 1)
                
        return longest
