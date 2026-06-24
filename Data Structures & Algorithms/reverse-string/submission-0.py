class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s)-1
        curr = ""

        while( left <= right):
            curr = s[left] 
            s[left] = s[right]
            s[right] = curr
            right -= 1
            left += 1
            


        """
        Do not return anything, modify s in-place instead.
        """
        