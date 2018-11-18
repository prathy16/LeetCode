'''
Problem: https://leetcode.com/problems/add-digits/
'''
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        m = 0
        while(num):
            m += num%10
            num = num//10
        if(m >= 10):
            return self.addDigits(m)
        return m
            
