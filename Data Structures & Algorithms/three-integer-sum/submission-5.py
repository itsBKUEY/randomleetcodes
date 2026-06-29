class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        arrayset = set()

        for i in range(0,len(nums)-1):   
            l = i+1
            r= len(nums)-1
            target = -nums[i]

            while(l<r):
                curr = nums[l] + nums[r]
                if curr == target:
                    
                    arrayset.add(tuple([nums[l],nums[r], nums[i]]))
                    l += 1
                    r -=1
                elif curr > target:
                    r -=1
                else:
                    l += 1

        return list(arrayset)
        

       




        
