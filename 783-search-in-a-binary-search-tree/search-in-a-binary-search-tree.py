# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return 

        def bst (node):
            if node is None:
                return

            if node.val == val:
                return node
            elif node.val > val:
                result=bst(node.left)
            elif node.val < val:
                result=bst(node.right)
            return result
        
        return bst(root)


        