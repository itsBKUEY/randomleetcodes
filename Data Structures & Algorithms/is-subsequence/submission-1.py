class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        count = 0

        for char in t:
            if(count >= len(s)):
                return True
            if(s[count] == char):
                count += 1
            
        if(count >= len(s)):
            return True

        
        return False
            
           
        