# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    
        if(not head):
            return 

        if(not head.next):
            return 
        
        if(not head.next.next):
            return 

       
        count = 0
        nodecount = head

        while(nodecount):
            count +=1
            nodecount = nodecount.next
        

        halflen = count//2
        breakpoint = head
        startpoint = head


        for _ in range(halflen):
           breakpoint = breakpoint.next

        prev = None

        while(breakpoint):
            temp = breakpoint.next
            breakpoint.next = prev
            prev = breakpoint
            breakpoint = temp

      

        while(prev.next and startpoint.next):   
            temp1 = startpoint.next
            temp2 = prev.next        
            
            prev.next = startpoint.next
            startpoint.next = prev
           
            prev = temp2
            startpoint = temp1
    

        return 