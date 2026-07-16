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


        curr = head 
        lengthcheck = head
        numb = n+1

        while(lengthcheck):
            lengthcheck = lengthcheck.next
    
            if( numb > 0):
                numb -= 1
            else:
                curr = curr.next

        if(numb > 0):
            return head.next

        if(curr):
            curr.next = curr.next.next
            return head
            
        curr = None

        return head


