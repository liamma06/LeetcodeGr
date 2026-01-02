# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        #Python lets you modify mutable objects (like lists) inside nested functions
        count = [0]

        #didn't know you can define a funciton inside a function good to know 
        def dfs(node,curMax):
            if node is None:
                return
            if node.val >= curMax:
                count[0] += 1
                curMax = node.val
            dfs(node.left, curMax )
            dfs(node.right,curMax)

        dfs(root,root.val)
        return count[0]