'''
Problem: https://leetcode.com/problems/search-a-2d-matrix-ii/
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(len(matrix) == 0 or len(matrix[0]) ==0):
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        
        row, col = rows-1, 0
        
        while(row >= 0 and row < rows and col >= 0 and col < cols):
            if(matrix[row][col] == target): 
                return True
            elif(matrix[row][col] < target):
                col += 1
            else:
                row -= 1
                
        return False
                
