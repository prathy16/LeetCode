'''
Problem: https://leetcode.com/problems/excel-sheet-column-number/submissions/
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        col_num = 0
        
        for c in s:
            col_num = col_num*26 + ord(c) - 64
            
        return col_num
