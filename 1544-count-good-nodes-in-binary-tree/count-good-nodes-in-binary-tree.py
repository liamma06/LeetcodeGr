# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
    curr node: 3 
    count = 1
    max = 3 
        node.right = 4
        count = 1
        max = 4  
            node.right = 5
            count = 2 
            max = 5
                node.right = None
                count = 0
                max = 5
                node.left = 1

"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float("-inf"))
        
    def dfs(self, node, max_so_far) -> int:
        if node is None:
            return 0 

        #we want to return some sort of count 
        count = 0
        if node.val >= max_so_far:
            count += 1 
            max_so_far = node.val

        count += self.dfs(node.right,max_so_far)
        count += self.dfs(node.left, max_so_far)

        return count 