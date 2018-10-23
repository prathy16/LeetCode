'''
Problem: https://leetcode.com/problems/roman-to-integer/
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result_sum = 0
        dict_romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        for i in range(len(s)-1):
            if(dict_romans[s[i]] >= dict_romans[s[i+1]]):
                result_sum += dict_romans[s[i]]
            else:
                result_sum -= dict_romans[s[i]]
                
        return (result_sum + dict_romans[s[-1]])
