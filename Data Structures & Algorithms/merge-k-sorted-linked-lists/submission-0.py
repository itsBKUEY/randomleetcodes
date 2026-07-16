# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#input : array of linkedlist
#output : linkedlist
# nothing in array

# current min 
#  loop through val of each and select  min
# for the that list head.next 
# until all are empty



class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(not lists):
            return  
        
        dummy = ListNode(-1)
        
        curr = dummy
        
        while(lists and curr):
            currmin = float('inf')
            currindex = -1

            for i in range(len(lists)):
                if lists[i] and currmin > lists[i].val:
                    currmin = lists[i].val
                    currindex = i

            curr.next = lists[currindex]
            curr = curr.next

            if(lists[currindex]):
                lists[currindex] = lists[currindex].next

        return dummy.next
            


        
                

            
                




        
