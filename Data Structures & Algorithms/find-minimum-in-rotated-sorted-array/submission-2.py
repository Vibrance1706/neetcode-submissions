class Solution:
    def findMin(self, nums: List[int]) -> int:
        # op_min = nums[0]
        # for val in nums:
        #     op_min = min(val, op_min)

        # return op_min
        op_min = nums[0]
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l]<nums[r]:
                op_min = min(nums[l], op_min)
                break
            
            mid = (l+r)//2
            op_min = min(nums[mid], op_min)
            if nums[mid]>=nums[l]:
                l = mid+1
            else:
                r=mid-1
        
        return op_min
