'''
Problem: https://leetcode.com/problems/palindrome-permutation/
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
'''
class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if len(s) is odd, then only one char can occur odd number of times
        # if len(s) is even, then all the char's should occur even no. of times
        charSet = set()
        
        for char in s:
            if char not in charSet:
                charSet.add(char)
            else:
                charSet.discard(char)
        
        if(len(s)%2 == 1):
            return len(charSet) == 1
        
        return len(charSet) == 0
