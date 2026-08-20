class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            temp_res = []
            for res in result:
                for i in range(len(res)+1):
                    res_copy = res.copy()
                    res_copy.insert(i, num)
                    temp_res.append(res_copy)
            result = temp_res
        
        return result

            
