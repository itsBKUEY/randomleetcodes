class Solution:

#input: string
#output: boolean

#Two pointer

#


    def validPalindrome(self, s: str) -> bool:
        loopFail = False
        for char in s:
            loopFail = False
            curs = s.replace(char,"")


            l = 0
            r = len(curs)-1
       

            while(l<r):
                while(not self.numericChecker(curs[l]) and l<r ):
                    l =+ 1
                while(not self.numericChecker(curs[l]) and l<r ):
                    r =- 1
            
                if(curs[l] == curs[r]):
                    l, r = l+1, r-1
                else:
                    loopFail = True
                    break
            if(loopFail != True):
                return True
            
        return False
                    


                




    def numericChecker(self, c) :
        return( ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))