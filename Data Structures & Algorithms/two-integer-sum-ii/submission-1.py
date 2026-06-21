class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j=0
        op_list=[]
        for i in range(len(numbers)):
            j=i+1
            for j in range(len(numbers)):
                if numbers[i] != numbers[j]:
                    if numbers[i]+numbers[j]==target:
                        op_list.append(i+1)
                        op_list.append(j+1)

                        return op_list
                    else:
                        continue
        
        
