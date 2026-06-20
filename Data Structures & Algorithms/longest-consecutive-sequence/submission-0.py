class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        nums.sort()
        longest=1
        current=1
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                i+=1
            elif nums[i]+1 == nums[i+1]:
                current+=1
                i+=1
            else:
                longest=max(longest,current)
                current=1
                i+=1
        
        k = max(longest,current)
        return k

