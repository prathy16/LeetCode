'''
Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
'''

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root and root.left:
            nextlevel = root.left
            while root:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
                else:
                    root.right.next = None

                root = root.next
            
            root = nextlevel
            
            
