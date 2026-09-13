# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
            -offset fast 
            -move togther until fast at the end 
            -slow next -> fast
        """

        #we ned dummy so if they ever remove head it still works 
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        #offset fast first need + 1 since we have dummy 1 behind
        for i in range(n+1):
            fast = fast.next

        #move togther until fast at the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        #skip one node (fast now none)
        slow.next = slow.next.next

        #dummy still points to start but next 
        return dummy.next
