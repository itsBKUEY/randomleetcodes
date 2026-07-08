# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

    
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(not head):
            return False
        if(not head.next):
            return True
        counterhead = head
        length = 0
        
        while(counterhead):
            length += 1
            counterhead = counterhead.next
            
        even = False
        if(length%2 == 0):
            even = True
        
        mid = length // 2
        counter = 0
        curr = head
        stack = []
        while (counter != mid):
            stack.append(curr.val)
            curr = curr.next
            counter += 1
        
        if not even:
            curr = curr.next
            
        while curr:
            if stack[-1] != curr.val:
                return False
            stack.pop()
            curr = curr.next
            
        return not stack
       
        