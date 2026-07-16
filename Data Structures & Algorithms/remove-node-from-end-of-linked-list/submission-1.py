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
        length = 0

        while(lengthcheck):
            lengthcheck = lengthcheck.next
            length += 1

            if( numb > 0):
                numb -= 1
            else:
                curr = curr.next

        if((length - n) <= 0):
            return head.next

        if(curr and curr.next and curr.next.next):
            curr.next = curr.next.next
            return head
        
        if(curr and curr.next):
            curr.next = None
            return head
            
        curr = None

        return head


