# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head 

        while curr:
            #save the next node 
            next_node = curr.next

            #shift the next to previous (at the start is none)
            curr.next = prev 

            #shift the prev to the current node 
            prev = curr

            #shiftover to the next node to repeat 
            curr = next_node
        
        return prev


