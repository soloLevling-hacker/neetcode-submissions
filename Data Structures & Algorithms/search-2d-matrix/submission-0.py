'''
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        raw = 0
        col = n-1

        while raw < m and col >= 0:
            val = matrix[raw][col]
            
            if val == target:
                return True
            elif val > target:
                col -= 1
            else:
                raw += 1
        return False