class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        while len(temperatures) !=0:
            rem_ele = temperatures.pop(0)
            j = 0
            day_count = 0
            found = False
            while j<len(temperatures):
                day_count+=1
                if temperatures[j] > rem_ele:
                    result.append(day_count)
                    found = True
                    break

                j+=1
            
            if not found:
                result.append(0)
                    

        return result
