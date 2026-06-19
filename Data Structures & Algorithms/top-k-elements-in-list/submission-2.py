class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        op_list = []
        for num in nums:
            if num not in num_freq:
                num_freq[num]=1
            else:
                num_freq[num]+=1
        
        num_freq_sorted = dict(sorted(num_freq.items(), key=lambda item: item[1], reverse=True))

        for i, (key, value) in enumerate(num_freq_sorted.items()):
            if i<k:
                op_list.append(key)
            

        
        return op_list
