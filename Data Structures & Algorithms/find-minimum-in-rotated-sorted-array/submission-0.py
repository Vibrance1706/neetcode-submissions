class Solution:
    def findMin(self, nums: List[int]) -> int:
        op_min = nums[0]
        for val in nums:
            op_min = min(val, op_min)

        return op_min
