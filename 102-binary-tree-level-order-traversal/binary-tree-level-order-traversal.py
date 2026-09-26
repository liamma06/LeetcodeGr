# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        result = []
        q = deque([root]) #put root in the quue

        while q:
            level_size = len(q) 
            level_val = []

            for _ in range(level_size):
                node = q.popleft() #take out of queue 
                level_val.append(node.val) #put in layer value

                #send the next left and right into the queue of next layer
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level_val)
        
        return result

