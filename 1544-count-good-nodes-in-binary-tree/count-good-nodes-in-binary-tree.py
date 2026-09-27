# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #root.val is max so far
        result = self.dfs(root,root.val)
        return result 


    def dfs(self,node, max_so_far):
        if node is None:
            return 0 
        
        if node.val >= max_so_far:
            count = 1 #always incrmeent by 1 if greater 
            new_max = max(max_so_far, node.val) #update
        else:
            count = 0 
            new_max = max_so_far

        left_count = self.dfs(node.left, new_max)
        right_count = self.dfs(node.right, new_max)

        return count + left_count + right_count #total count of what good

    """
        Using "global" variable 
        def goodNodes(self, root: TreeNode) -> int:
            self.count = 0 
            self.dfs(root, root.val)
            return self.count

        def dfs(self, node, max_so_far):
            if node is None:
                return 

            if node.val >= max_so_far:
                self.count += 1 

            new_max = max(max_so_far, node.val)
            self.dfs(node.left, new_max)
            self.dfs(node.right,new_max)
    """
        