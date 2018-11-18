'''
Problem: https://leetcode.com/problems/self-dividing-numbers/submissions/
'''

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isSelfDividingNum(n):
            if(n<10): 
                return True
            
            k, m = 0, n
            
            while(k == 0 and n > 0):
                r, n = n%10, n//10

                if(r == 0): 
                    return False
                
                k = m % r
                
            if(k!=0): 
                return False
            return True
        
        nums = []
        
        for n in range(left, right+1):
            if isSelfDividingNum(n):
                nums.append(n)
                
        return nums
