# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        result = self.height(root)
         
        if result == -1:
            return False 
        return True 
        

    def height(self,root):
        if root is None:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)

        #conditions of fails 
        if left == -1 or right == -1:
            return -1
        
        if abs(left-right) > 1:
            return -1

        height = 1+ max(left,right)
        return height 

        