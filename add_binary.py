'''
Problem: https://leetcode.com/problems/add-binary
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        if(len(a) == 0): return b
        if(len(b) == 0): return a
        
        if(a[-1] == '1' and b[-1] == '1'):
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        else:
            return self.addBinary(a[:-1], b[:-1])+str(int(a[-1])+int(b[-1]))
        
