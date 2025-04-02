# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isGood(target):
            tot_sum = 0
            subarray = 0
            for num in nums:
                tot_sum += num
                if tot_sum > target:
                    subarray += 1
                    tot_sum = num
            return subarray + 1 <= k

        left = max(nums)
        right  = sum(nums)
        ans = right

        while left <= right:
            mid = (left + right) // 2

            if isGood(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans