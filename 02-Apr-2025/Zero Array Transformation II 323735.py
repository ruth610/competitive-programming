# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def found(target):
            size = len(nums)
            my_array = [0]*(size)
            for i in range(target):
                l , r, val = queries[i]
                my_array[l] += val
                if r + 1 < size:
                    my_array[r+1] -= val
            current_decrement = 0
            for i in range(size):
                current_decrement += my_array[i]
                if nums[i] > current_decrement:
                    return False
            
            return True

        left = 0
        right = len(queries)
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if found(mid):
                ans = mid 
                right = mid - 1
            else:
                left = mid + 1
        return ans

