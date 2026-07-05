class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l = 0
        r = len(nums)-1
       
            


        while (l<r):
            m = (l+r) // 2
            if(nums[m] < nums[r]):
                print("")
                print(nums)
                print("nums[l] < nums[m]")
                print("nums[l]", nums[l])
                print("nums[m]", nums[m])
                print("nums[r]", nums[r])
                print("")

                r = m
                
            else:
                print("")
                print(nums)
                print("NOT nums[m] < nums[r]")
                print("nums[l]", nums[l])
                print("nums[m]", nums[m])
                print("nums[r]", nums[r])
                print("")
                l = m+1

        return nums[l]
