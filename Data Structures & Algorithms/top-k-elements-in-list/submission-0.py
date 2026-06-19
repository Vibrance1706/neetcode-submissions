class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        op_list = []
        for num in nums:
            if num not in num_freq:
                num_freq[num]=1
            else:
                num_freq[num]+=1
        
        for idx in num_freq:
            if num_freq[idx] >= k:
                op_list.append(idx)
        
        return op_list
