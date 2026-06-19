class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = list(nums)
        new_nums.sort()
        for i in range(len(new_nums) - 1):
            if new_nums[i] == new_nums[i+1]:
                return True
        return False