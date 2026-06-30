class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_row = len(matrix)
        len_col = len(matrix[0])
        i, j = 0, len_col-1
        found = False
        while i<len_row and j>=0:
            if matrix[i][j]<target:
                i +=1
                found = False
            elif matrix[i][j]>target:
                j -=1
                found = False
            else:
                found = True
                break

        return found



