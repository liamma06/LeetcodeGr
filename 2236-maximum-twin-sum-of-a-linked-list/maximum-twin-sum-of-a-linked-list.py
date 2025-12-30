# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        #find middle 
        mid = head
        fast = head

        while fast is not None and fast.next is not None:
            mid = mid.next
            fast = fast.next.next
        
        #reverse second 
        prev = None
        curr = mid 

        while curr is not None:
            nxt = curr.next
            curr.next= prev
            prev = curr
            curr = nxt

        #add as you loop thorugh 
        left = head 
        right = prev
        maxRn = 0

        while right is not None:
            maxRn = max(maxRn , left.val+right.val)
            left = left.next
            right = right.next
        
        return maxRn
        