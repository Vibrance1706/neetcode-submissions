class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_sub_list = []
        op_list = []
        i=0
        while i <= len(nums)-k:
            sub_list = []
            j = i+k-1
            g=i
            while g<=j and j<len(nums):
                sub_list.append(nums[g])
                g+=1
            
            max_sub_list.append(sub_list)
            i+=1

        for sub_list in max_sub_list:
            sub_list.sort()
            op_list.append(sub_list[-1])
        
        return op_list
        
                

