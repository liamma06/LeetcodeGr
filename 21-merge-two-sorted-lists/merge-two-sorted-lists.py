# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list2.val <= list1.val:
                #if less or equal make it next 
                tail.next = list2

                #increment 
                list2 = list2.next
                tail = tail.next
            else:
                tail.next = list1

                list1 = list1.next
                tail = tail.next

        #since and means if one of them done then we just attach waht left 

        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        #that is the start is dummy is just an empty node after is when it starts 
        return dummy.next

        