class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num]=1
            else:
                nums_dict[num]+=1

        op_list = [item[0] for item in sorted(nums_dict.items(), key=lambda item: item[1], reverse=True)[:k]]


        return op_list

        

        