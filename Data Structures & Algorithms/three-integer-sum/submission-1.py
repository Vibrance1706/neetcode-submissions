# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         # j,k=0,0
#         # nums.sort()
#         # op_list=[]
#         # for i in range(len(nums)):
#         #     j=i+1
#         #     for j in range(len(nums)):
#         #         k=j+2
#         #         for k in range(len(nums)):
#         #             append_list = []
#         #             if nums[i]+nums[j]+nums[k]==0 and i!=j and j!=k and i!=k:
#         #                 append_list.extend([nums[i], nums[j], nums[k]])
#         #                 append_list.sort()
#         #                 if append_list not in op_list:
#         #                     op_list.append(append_list)
                    
#         # return op_list
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        op_list = []

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                append_list = []
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    append_list.extend([nums[i], nums[j], nums[k]])

                    if append_list not in op_list:
                        op_list.append(append_list)

                    j += 1
                    k -= 1

                elif total < 0:
                    j += 1

                else:
                    k -= 1

        return op_list

