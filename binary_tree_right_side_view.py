'''
Problem: https://leetcode.com/problems/binary-tree-right-side-view/
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def __init__(self):
        self.rightView = []
        self.maxlevel = 0
        
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root, level):
            if root is None:
                return 
            
            if self.maxlevel < level:
                self.rightView.append(root.val)
                self.maxlevel = level
                
            helper(root.right, level+1)
            helper(root.left, level+1)
            
        helper(root, 1)
        return self.rightView
