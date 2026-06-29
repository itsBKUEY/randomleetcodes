class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        arrayset = set()

        for i in range(0,len(nums)-1): 
            if i > 0 and nums[i] == nums[i-1]:
                continue  

            l = i+1
            r= len(nums)-1
            target = -nums[i]

            while(l<r):
               
                curr = nums[l] + nums[r]
                if curr == target:
                    arrayset.add((nums[l],nums[r], nums[i]))
                    l += 1
                    r -=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif curr > target:
                    r -=1
                else:
                    l += 1
        print(arrayset)
        return list(arrayset)
        

       
