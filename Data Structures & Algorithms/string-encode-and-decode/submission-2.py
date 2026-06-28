class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "[]"
        
        newstring = ""

        for i in range(len(strs)):
            newstring += (strs[i])

            if (i != len(strs)-1):
                newstring += "+@!$"
            
        return newstring

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        return list(s.split("+@!$"))
        
