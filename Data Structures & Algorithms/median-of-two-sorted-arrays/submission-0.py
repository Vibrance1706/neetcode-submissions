class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_nums = nums1+nums2
        new_nums.sort()
        len_new_nums = len(new_nums)
        if len_new_nums % 2 == 0:
            a = new_nums[len_new_nums//2]
            b = new_nums[(len_new_nums//2)-1]
            median = (a+b)/2
        else:
            median = new_nums[len_new_nums//2]
        
        return median
