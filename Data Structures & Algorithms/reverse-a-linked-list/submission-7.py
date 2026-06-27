# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# O <- O <- O <- O
#.        
#

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
       
        if not (head):
            return head
        
        if not (head.next):
            return head
        
        prev = head
        curr = head.next
        if(curr):
            nxt = curr.next
        else:
            nxt =  None
            
        prev.next = None

        while(nxt):
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
        
        curr.next = prev

        return curr
