# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])


        left , right = 0, row * col -1
        while left <= right:
            mid  = (left + right) // 2
            mid_value = matrix[mid // col][mid % col]

            if mid_value== target:
                return True
            elif mid_value < target:
                left = mid + 1

            else:
                right = mid - 1
        return False
