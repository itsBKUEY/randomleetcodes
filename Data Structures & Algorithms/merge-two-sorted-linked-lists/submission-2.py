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

        p1 = list1
        p2 = list2

        if not (p1):
            return p2
        if not (p2):
            return p1
       
        if(p1.val <= p2.val):
            start = p1
            p1 = p1.next
        else:
            start = p2
            p2 = p2.next
        
        startstart = start

        while(p1 and p2):
            
            if(p1.val <= p2.val):
                start.next = p1
                start = start.next
                p1 = p1.next
            else:
                start.next = p2
                start = start.next
                p2 = p2.next
            
        if(p1):
            print("p1",p1.val)
            start.next = p1
        elif(p2):
            print("p2",p2.val)
            start.next = p2

        

        return startstart

            