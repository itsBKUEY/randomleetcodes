class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        freqmap = dict()
                    
        for i in range(len(magazine)):
            if magazine[i] in freqmap:
                freqmap[magazine[i]] += 1
            else:
                freqmap[magazine[i]] = 1
                    
            
        for i in range(len(ransomNote)):
            if ransomNote[i] in freqmap and freqmap[ransomNote[i]] > 0:
                freqmap[ransomNote[i]] -= 1
            else: 
                return False
            
        return True
        