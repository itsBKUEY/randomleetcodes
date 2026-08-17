class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def subsethelper(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            subsethelper(i+1)
            subset.pop()
            subsethelper(i+1)
    
        subsethelper(0)
        return res

            
