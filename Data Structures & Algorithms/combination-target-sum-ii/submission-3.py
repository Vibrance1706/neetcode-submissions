class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(start, target, curr):
            if target == 0:
                result.append(curr.copy())
                return
            
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                
                curr.append(candidates[i])
                backtrack(i+1, target - candidates[i], curr)
                curr.pop()
            
        backtrack(0, target, [])
        return result