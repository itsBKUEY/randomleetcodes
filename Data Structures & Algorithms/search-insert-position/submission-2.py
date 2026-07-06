class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        print(nums)
        
        while(l <=  r):
            m = (l+r)//2
            if(nums[m] == target):
                return m
            elif(target > nums[m]):
                l = m+1
                print("left")
            else:
                r = m-1
                print("right")
        

        print("before", m)
        
        print("after", m)

        

        if( nums[m] < target ):
            m = (l+r)//2
            return m+1
        else:
            
            return m

      
