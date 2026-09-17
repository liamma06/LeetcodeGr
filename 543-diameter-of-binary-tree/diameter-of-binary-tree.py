# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0 

        self.height(root)

        return self.max_diameter

    def height(self, root):
        if root is None:
            return 0 
        
        left = self.height(root.left)
        right = self.height(root.right)

        #finding the deepest part of the the current node 
        deepest = max(left, right) + 1 

        #comparing the deepest of both sides against each other for max_diameter
        self.max_diameter = max(left + right, self.max_diameter)

        return deepest