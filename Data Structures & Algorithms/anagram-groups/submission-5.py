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
        base = ord('a')
        for word in strs:
            charIndex = [0] *26
            
            for char in word:
                charIndex[ord(char) - base] += 1
            #since you need to input it as a static array since you can't input dynaimic elements as keys make it a tuple
            key = tuple(charIndex)
            if(key in higherdict):
                higherdict[key].append(word)
            else:
                higherdict[key] = [word]
        
        result = list(higherdict.values())
        return result
