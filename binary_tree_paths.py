'''
Problem: https://leetcode.com/problems/binary-tree-paths/
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # empty tree
        if not root: 
            return []
        
        # root node with no children
        if not root.left and not root.right:
            return [str(root.val)]
        
        # node with only right child
        if not root.left:
            return [str(root.val)+"->"+item for item in self.binaryTreePaths(root.right)]
        
        # node with only left child
        if not root.right:
            return [str(root.val)+"->"+item for item in self.binaryTreePaths(root.left)]
        
        # node with both children
        ret_list = [str(root.val)+"->"+item for item in self.binaryTreePaths(root.left)]
        
        ret_list.extend([str(root.val)+"->"+item for item in self.binaryTreePaths(root.right)])
        
        return ret_list
