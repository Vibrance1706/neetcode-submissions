class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        op_list = []
        for num in nums:
            if num not in op_list:
                op_list.append(num)
            else:
                return num
        
