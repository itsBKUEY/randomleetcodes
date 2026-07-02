class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setnums = set(nums)
    
        maxlength = 0

        for num in setnums:
            if num-1 in setnums:
                continue

            length = 0
                    

            while(num in setnums):
                length +=1
                num = num+1
                    
            maxlength = max(length,maxlength)

        return maxlength
                    

            
        