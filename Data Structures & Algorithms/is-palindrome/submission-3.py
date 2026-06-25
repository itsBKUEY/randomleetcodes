class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def checker(char):
            return not (ord("a") <= ord(char) <= ord("z") 
            or ord("0") <= ord(char) <= ord("9"))

        s = s.lower()
        l = 0
        r = len(s)-1

        while(l < r):
            while( checker(s[l]) and l < r ):
                l += 1

            while( checker(s[r]) and l < r ):
                r -= 1

            if(s[l] != s[r]):
                return False
           
            r, l = r-1, l+1
    
            


        return True
