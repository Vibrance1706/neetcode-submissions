class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        op_list = []
        while i<len(nums):
            j=i+1
            while j<len(nums):
                if i!=j and nums[i]+nums[j]==target:
                    op_list.append(i)
                    op_list.append(j)
                    break

                j+=1
            i+=1
        
        return op_list
                    

