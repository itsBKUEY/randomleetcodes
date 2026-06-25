class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        
        stack = []

 

        for char in s:
            if char in hashmap.values():
                stack.append(char)
            elif(stack):
                if(stack.pop()!= hashmap[char]):
                        return False     
            else:
                return False

        if(stack):
            return False
        else:
            return True


        