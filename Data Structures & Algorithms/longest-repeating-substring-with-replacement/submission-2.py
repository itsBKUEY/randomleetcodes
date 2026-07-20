class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqmap = dict()
        
        result = 0
        slow = 0
        maxf = 0

        for fast in range(len(s)):
            freqmap[s[fast]] = freqmap.get(s[fast], 0) + 1
            print(freqmap)
            maxf = max(maxf, freqmap[s[fast]])
            print("maxf", maxf)
            print("entering loop")
            print("")
            while( (fast-slow)+1 - maxf > k):
                print("")
              
                print("length", fast-slow )
                print("freqmap", freqmap[s[slow]])
                print("slow: ", slow)
                print("")
                freqmap[s[slow]] -= 1
                slow += 1
                print("Updated length", fast-slow )
                print("Updated freqmap", freqmap[s[slow]])
                print("Updated slow: ", slow)
                print(" ")
                
            print("")
            print("exiting loop")
      
            result = max((fast-slow)+1 ,result)   


        return result
            

