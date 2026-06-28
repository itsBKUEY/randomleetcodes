class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexmap = dict()

        for i in range(len(nums)):
            if nums[i] in indexmap:
                return [indexmap[nums[i]],i]
            else:
                indexmap[target-nums[i]] = i
        
        return -1