'''
Problem: https://leetcode.com/problems/implement-strstr/submissions/
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, m = len(haystack), len(needle)
        
        if(n == 0 and m == 0): 
            return 0
        elif(n == 0):
            return -1
        elif(m == 0):
            return 0
        
        i = 0
        
        while(i < n-m+1):
            if(haystack[i] == needle[0]):
                if(haystack[i:i+m] == needle):
                    return i
                else:
                    i = i + 1
            else:
                i = i + 1
                
        return -1
                    
            
                
