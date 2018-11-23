'''
Problem: https://leetcode.com/problems/rotate-image/
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
    
        rows = len(matrix)
        if(rows == 0): 
            return matrix
        
        cols = len(matrix[0])
        matrix[:] = matrix[::-1]

        for i in range(rows):
            for j in range(i+1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
                
        
