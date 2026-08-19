class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, target, curr):
            if target == 0:
                result.append(curr.copy())
                return
            
            if target < 0:
                return
            
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i, target - nums[i], curr)
                curr.pop()

        backtrack(0, target, [])
        return result
