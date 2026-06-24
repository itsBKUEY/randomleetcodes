#INPUT : array of ints and int


#OUTPUT: array -> [int,int]


#METHOD: dictionary 

# dictioanry [(Target- number), index]
# return [currindex which is {(Target- number)}, index]







class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictnumbs = {}
       
        

        for i in range(len(nums)):
            if nums[i] in dictnumbs:
                return [dictnumbs[nums[i]], i]
            else:
                dictnumbs[target-nums[i]] = i
        return -1



                
        
        
