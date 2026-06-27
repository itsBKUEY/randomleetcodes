# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
## O-> O -> O -> O->
#. ~. <-~.   ~

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head: 
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        
        return prev

