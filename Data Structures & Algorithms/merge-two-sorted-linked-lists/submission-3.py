# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#.    1 -> 2 -> 4
#.    p1.  
#.    1 -> 3 -> 5
#.    p2

# 
#
# if p1 <= p2
#.   start = p1
#.   p1 = p1.next
#  else:
#.   start = p2
#.   p2 = p2.next
#    
#while(p1 or p2)
#.   if p1 <= p2
#.   start.next = p1
#.   p1 = p1.next
#      start = starnext
#  else:
#.   start = p2
#.   p2 = p2.next
#    
#
#.   

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while(list1 and list2):
            if( list1.val <= list2.val):
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if(list2):
            tail.next = list2
        if(list1):
            tail.next = list1

        return dummy.next

            