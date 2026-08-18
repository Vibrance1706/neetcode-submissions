class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        i = 0
        len_nums = len(nums)
        op_list=[[]]
        while i<len_nums:
            j = 0
            curr_len = len(op_list)
            while j<curr_len:
                lis = op_list[j]+[nums[i]]
                op_list.append(lis)
                j+=1

            if lis not in op_list:
                op_list.append(lis)

            i+=1

        return op_list[::-1]