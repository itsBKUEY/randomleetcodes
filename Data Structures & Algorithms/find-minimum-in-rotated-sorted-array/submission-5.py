class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[0]

        while(l<=r):        
            if(nums[r] > nums[l]):
                #check if it's sorted
                res = min(res, nums[l])
                break
            

            m = (l+r)//2
            #check if current one is lowest
            res = min(res,nums[m])

            if(nums[m] >= nums[l]):
                #search right since we know it's not sorted and m is greater meaning it's in the first section
                l = m+1
            else:
                #search left since we know it's not sorted and m is meaning it's in the first section
                r = m-1
        
        return res
        
