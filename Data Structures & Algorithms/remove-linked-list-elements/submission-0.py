# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #create dummy node
        #remove 

        if(not head):
            return

        dummy = ListNode(0, head)

        curr = head
        prev = dummy


        while(curr):
            temp = curr.next
            print("temp",temp)
            print("prev.next  b4",prev.next.val )
            if(curr.val == val):
                prev.next = temp
            else:
                prev = curr
            curr = temp

        
        return dummy.next



