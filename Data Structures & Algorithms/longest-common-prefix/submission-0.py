class Solution:

    #stack that contains each prefix option
    # d. da - dan -danc - dance 
    #use list length to determine length that will be tested

    #go to through the loop
    #if len(word ) is longer pop until len(stack) == word

    #if word not stack item pop until is.
    #move to next word

    def longestCommonPrefix(self, strs: List[str]) -> str:
        stack = []
        word = ""

        for prefixes in strs[0]:
            word += prefixes
            stack.append(word)

        for word in strs:
            slicedword = word[0:len(stack)]

            while(stack and stack[-1] != slicedword): 
                stack.pop()
                slicedword = word[0:len(stack)]



        
        if(stack):
            return stack[-1]
        else: 
            return ""



                
                
                    
                    
