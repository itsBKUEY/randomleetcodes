class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length =0
        for i in range(len(s)):
            if(s[i] == " " ):
                if(length !=0):
                    last = length
                length = 0
            else:
                length +=1
                
        if(length != 0):
            return length
        else:
            return last
