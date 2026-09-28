# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(not head):
            return

        count = 0
        countnode = head

        while(countnode):
            count += 1
            countnode = countnode.next

        middle = (count // 2)

        for i in range(middle):
            head = head.next


        return head


