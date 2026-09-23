# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if (p is None and q is None):
            return True
        elif (p is None or q is None):
            return False
        else: 
            if q.val == p.val:
                
                left_same = self.isSameTree(p.right, q.right)
                right_same = self.isSameTree(p.left, q.left)
                return left_same and right_same

            else:
                return False