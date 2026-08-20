class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        result = [[]]
        for num in nums:
            temp_res = []
            for ele in result:
                    ele_copy = ele.copy()
                    ele_copy.append(num)
                    ele_copy.sort()
                    if ele_copy not in result and ele_copy not in temp_res:
                        temp_res.append(ele_copy) 

            result.extend(temp_res)

        return result
