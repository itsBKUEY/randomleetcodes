class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        # 1,1,2,

        return nums[len(nums)-k]