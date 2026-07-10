class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        #each char within string0
        for i in range(len(strs[0])):
            #each string
            for s in strs:
                #check if  within range of s and if char of the string is the same as the first string
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res
                
        