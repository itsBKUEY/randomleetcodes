class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqmap = dict()

        if(len(s) != len(t)):
            return False

        for char in s:
            if(char in freqmap):
                freqmap[char] += 1
            else:
                freqmap[char] = 1

        for char in t:
            if(char in freqmap and freqmap[char] > 0 ):
                freqmap[char] -= 1
            else:
                return False   
 
        return True