# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        longest = [0]

        def maxZigZag(node,direction,currSum):
            if node is None:
                return 

            if node.left is not None:
                if direction == "right":
                    newLen = currSum+1
                else:
                    newLen= 1
                maxZigZag(node.left,"left",newLen)
            if node.right is not None:
                if direction == "left":
                    newLen = currSum+1
                else:
                    newLen= 1
                maxZigZag(node.right,"right",newLen)

            longest[0] = max(currSum,longest[0])
       
        maxZigZag(root, "left", 0)
        maxZigZag(root, "right", 0)
    
        return longest[0]
            

            