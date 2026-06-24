class Solution:
    #INPUT: STRING
    #OUTPUT: BOOL

    #TASK: CHECK IF ANAGRAM 

    

    def isAnagram(self, s: str, t: str) -> bool:
        anaDict = dict()
        #freq map
        if(len(s) != len(t)):
            return False
            
        for char in s:
            if( char in anaDict):
                anaDict[char] += 1
            else:
                anaDict[char] = 1

        print(anaDict)
        for chart in t:
            if( chart in anaDict):
                if(anaDict[chart] >= 1):
                    anaDict[chart] -= 1
                else:
                    return False
            else:
                return False
        return True
