# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        #both less then search left since BST
        if p.val < root.val and q.val < root.val:
            ans = self.lowestCommonAncestor(root.left, p, q)
            return ans
        
        #both greater 
        elif p.val > root.val and q.val > root.val:
            ans = self.lowestCommonAncestor(root.right, p, q)
            return ans
        else:
            return root

        

