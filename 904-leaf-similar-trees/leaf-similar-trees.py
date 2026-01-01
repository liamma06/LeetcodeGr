# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#IMPROTANT LESSON: SELF referenes to the the class so when you call dfs it says within itsefl(class) use this function dfs
class Solution:
    def dfs(self,node,leaves):
        if node is None:
            return

        if node.left is None and node.right is None:
            leaves.append(node.val)
            return

        self.dfs(node.left, leaves)
        self.dfs(node.right,leaves)
        return leaves

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1= []
        leaves2 = [] 

        self.dfs(root1,leaves1)                    
        self.dfs(root2,leaves2)
        return leaves1 == leaves2
        