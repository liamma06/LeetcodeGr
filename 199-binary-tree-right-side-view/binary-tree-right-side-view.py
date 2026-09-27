# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        output = [] 

        q = deque([root])

        while q:
            #how many elements this level 
            level_size = len(q) 
            level_store = [] 

            for _ in range(level_size):

                #take out and store 
                node = q.popleft()
                level_store.append(node.val)

                #queue next nodes/level to be checkedd 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            #only put in the right most value
            output.append(level_store[-1])
        return output 
