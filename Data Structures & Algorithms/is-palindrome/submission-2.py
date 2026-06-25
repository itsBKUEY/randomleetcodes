class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def checker(char):
            if(ord("a") <= ord(char) <= ord("z") 
            or ord("A") <= ord(char) <= ord("Z") 
            or ord("0") <= ord(char) <= ord("9")
            ):
                return True
            else:
                return False
        
        s = s.lower()

        l = 0
        r = len(s)-1

        while(l < r):
            while(not checker(s[l]) and l < r ):
                print(checker(s[l]))    
                l += 1

            while(not checker(s[r]) and l < r ):
                print(checker(s[r]))
                r -= 1

            print("l",l)
            print("r",r)
            print(s[l], "=", s[r])

            if(s[l] != s[r]):
                return False
           
            l += 1
            r -= 1
            


        return True
