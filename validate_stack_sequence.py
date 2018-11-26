'''
Problem: https://leetcode.com/problems/validate-stack-sequences/
'''

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        pushInd, popInd = 0, 0
        
        while (pushInd < len(pushed)):
            if pushed[pushInd] == popped[popInd]:
                popInd += 1
                pushInd += 1
            elif len(stack) > 0 and stack[-1] == popped[popInd]:
                stack.pop()
                popInd += 1
            else:
                stack.append(pushed[pushInd])
                pushInd += 1
                
        while(stack and popInd < len(popped)):
            if stack.pop() == popped[popInd]:
                popInd += 1
            else:
                return False
            
        return True
