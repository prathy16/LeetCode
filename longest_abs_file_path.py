'''
Problem: https://leetcode.com/problems/longest-absolute-file-path/
'''

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlength = 0
        path = []
        
        for line in input.split('\n'):
            path[line.count('\t'):] = [len(line.strip('\t'))]
            if '.' in line:
                maxlength = max(maxlength, sum(path) + len(path) - 1)
                
        return maxlength
