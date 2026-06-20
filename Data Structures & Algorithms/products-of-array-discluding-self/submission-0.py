class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_nums = list(nums)
        len_nums = len(nums)
        op=[]

        i=0
        while i < len_nums:
            pdt = 1

            rem_ele = new_nums.pop(i)

            j=0
            while j < len(new_nums):
                pdt = pdt * new_nums[j]
                j+=1
            
            new_nums.insert(i, rem_ele)
            op.append(pdt)
            i+=1
        
        return op
        