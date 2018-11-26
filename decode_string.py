'''
Problem: https://leetcode.com/problems/decode-string/
'''

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curNum = 0
        curStr = ''
        
        for i in range(len(s)):
            if s[i] == '[':
                stack.append(curStr)
                stack.append(curNum)
                curStr = ''
                curNum = 0
            
            elif s[i] == ']':
                num = stack.pop()
                prevstr = stack.pop()
                curStr = prevstr + num*curStr
            
            elif s[i].isdigit():
                curNum = curNum*10 + int(s[i])
                
            else:
                curStr += s[i]
                
        return curStr
