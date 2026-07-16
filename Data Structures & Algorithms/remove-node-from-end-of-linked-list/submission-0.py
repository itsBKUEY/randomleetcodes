# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(not head):
            return 

        if(not head.next):
            return

        lengthcheck = head
        length = 0

        while(lengthcheck):
            length += 1
            lengthcheck = lengthcheck.next
       
        removePoint = length-n

        curr = head 


        if(removePoint <= 0):
            return head.next

        while(curr and removePoint > 1  ):
            removePoint -= 1
            curr = curr.next
        
        if(curr.next.next):
            curr.next = curr.next.next
            return head
        
        if(curr.next):
            curr.next = None
            return head
            
        curr = None

        return head


