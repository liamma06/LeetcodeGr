# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        """
            Find middle take the 2nd half reverse and intertin 
        """

        if not head or not head.next:
            return

        #to find middle can have one go twice as fast until it gets oteh end and slow would be middle (1 past)

        prev = None 
        slow = head 
        fast = head

        while fast and fast.next:
            #to properly store the node 
            prev = slow 

            slow = slow.next
            fast = fast.next.next

        #split into two halfs (head 1st, slow 2nd)
        prev.next = None

        #reverse 2nd half
        curr = slow
        prev = None

        while curr:
            next_node = curr.next 
            curr.next = prev

            #prev now stores the head 
            prev = curr
            curr = next_node

        #merge togther 
        dummy = ListNode()
        tail = dummy

        while prev and head:
            #store 
            first_next = head.next
            second_next = prev.next

            #increment and shift tail over too 
            tail.next = head
            tail = tail.next

            #same for the second half 
            tail.next = prev 
            tail = tail.next 

            #increment the two. 
            head = first_next
            prev = second_next 
        
        #in the odd senario there should be left over so just add it to the end 
        if prev:
            tail.next = prev

        return


            