# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# O <- O <- O -> O
#          P.    H.   T
#

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
       
        if not (head):
            return head

        while(head.next):
            temp =  head.next
            head.next = prev
            prev = head
            if(temp):
                head = temp


        head.next = prev

        return head
