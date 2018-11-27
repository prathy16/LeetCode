'''
Problem: https://leetcode.com/problems/friend-circles/
'''

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(M, visited, i):
            for j in range(len(M)):
                if M[i][j] == 1 and visited[j] == False:
                    visited[j] = True
                    dfs(M, visited, j)
                
            
        visited = [False for i in range(len(M))]
        count = 0
        for i in range(len(M)):
            if visited[i] == False:
                visited[i] = True
                dfs(M, visited, i)
                count += 1
                
        return count
