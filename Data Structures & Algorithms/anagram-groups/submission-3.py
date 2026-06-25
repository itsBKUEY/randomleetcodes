class Solution:
    #input:  array of stings

    #output:  array of arrays of strings

    #goal group each annagram up


    # make each string into a set
    # if string matches with set
    # group 
    #else
    # make new group


    #  greatarray
    # higherdict = {}

    #For word in array
    # set = makeset(word)
    # if set in higherdict:
    #   higherdict[set].append(word)
    # else
    # higherdict[set] = [word]
    #

    #for keys through higher dict
    #    greatarray.append.higherdict[key]
    #
    # return greatarray
    #

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        higherdict = dict()
        
        for word in strs:
            charIndex = [0] *26
            
            for char in word:
                charIndex[ord(char) - ord('a')] += 1
            if(tuple(charIndex) in higherdict):
                higherdict[tuple(charIndex)].append(word)
            else:
                higherdict[tuple(charIndex)] = [word]
    
        return list(higherdict.values())
