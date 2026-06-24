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
            
            
                if(curs[l] == curs[r]):
                    l, r = l+1, r-1
                else:
                    loopFail = True
                    break
            if(loopFail != True):
                return True
            
        return False
                    


            

