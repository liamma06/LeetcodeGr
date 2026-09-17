# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0 # zero not none since can't comapre nones 

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        #+ 1 since it includes the current node 
        max_depth = max(left_depth, right_depth) + 1 
    
        return max_depth