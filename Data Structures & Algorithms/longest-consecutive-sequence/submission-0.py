# 9, 8, 4, 3, 6, 7, 5,


#hashset[9] = 1
#hashset[8] = 2
#hashset[4] = 1
#hashset[3] = 2
#hashset[6] = 1

#hashset[7] = 3
#hashset[6] = 4

#hashset[5] = 5
#hashset[4] = 6


#hashset[9] = 1
#hashset[8] = 1







class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxvalue = 0


        for numb in hashset:
            #check is the start
            if numb-1 in hashset:
                continue
                
            seqlength = 1

            while(numb+1 in hashset):
                seqlength += 1
                numb = numb+1
            
            maxvalue = max(maxvalue,seqlength)

        return maxvalue
           
            

            