# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #if only one number
        if head.next is None:
            return None

        prev = None
        current = head
        fast = head

        while fast is not None and fast.next is not None:
            prev = current 
            current = current.next
            fast = fast.next.next
        
        prev.next = current.next

        return head


        