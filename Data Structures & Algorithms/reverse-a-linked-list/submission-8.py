# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O <- O -> O -> O
# .      TF. 
#


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        fast = head
        

        while(fast):

            print("fast", fast.val)
            print("FAST NEXT:", fast.next)

            temp = fast.next
            fast.next = prev

            prev = fast
            fast = temp

        
        return prev
            


            