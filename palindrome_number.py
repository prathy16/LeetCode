'''
Problem: https://leetcode.com/problems/palindrome-number/submissions/
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        def palindrome(x):
            """
            :type x: str
            :rtype : bool 
            """
            if(len(x) < 2): return True
            if(x[0] == x[-1]):
                return palindrome(x[1:-1])
            else:
                return False
        if(x < 0): return False
        return palindrome(str(x))
