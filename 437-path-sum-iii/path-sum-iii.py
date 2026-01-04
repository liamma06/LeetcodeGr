# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0 
        
        count = [0]

        def dfs(node,pathSum):
            if node is None:
                return
            pathSum = pathSum + node.val

            if pathSum == targetSum:
                count[0] +=1
            dfs(node.left,pathSum)
            dfs(node.right,pathSum)
        
        dfs(root,0)
        
        #this part took me a bit to figure out 
         #everyone has this own path so you need to call it for the indivdual and add it in 
        count[0]+=self.pathSum(root.left,targetSum)
        count[0] += self.pathSum(root.right,targetSum)
        return count[0]