class Solution:

    #pass through array
    #multply each by i
    #if we detect zero then 
    #   zero = true
    #   zeroindex = i

    #if we detect zero index 
    # make full array zero
    # make zero index product

    #product toatal(no zero) : 48

    #edge case: 0 division

    #passs through  num[i]= total/num[i]
    #return that

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero = False
        zeroindex = -1
        print(len(nums))
        

        for i in range(len(nums)):
            if(nums[i] == 0 and zero == False ):
                zero = True
                zeroindex = i
            else:
                total = total * nums[i]

        if(zero):
            for i in range(len(nums)):
                nums[i] = 0
            
            nums[zeroindex] = total

        else:
            for i in range(len(nums)):
                nums[i] = total//nums[i]

        return nums
        
        


        