# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if root is None:
            return False

        #check if match
        if self.isSameTree(root, subRoot):
            return True
        
        #since it doens''t match recurse thorugh 
        right_ans = self.isSubtree(root.right,subRoot)
        left_ans = self.isSubtree(root.left,subRoot)
        return right_ans or left_ans


    
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
        