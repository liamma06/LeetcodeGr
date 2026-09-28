# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.count = 0
        self.answer = None
        self.k = k
        self.dfs(root)

        return self.answer 

    def dfs(self,node):
        if node is None:
            return 
        
        #leave early 
        if self.answer != None:
            return 
        
        #go all the way left 
        self.dfs(node.left)

        self.count += 1
        
        #left if least so increment and shift right until it matches 
        if self.count == self.k :
            self.answer = node.val
            return 

        self.dfs(node.right) 