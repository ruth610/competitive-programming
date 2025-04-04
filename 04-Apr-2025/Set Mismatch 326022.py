# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0 
        while i < n:
            if nums[i] != i + 1:
                if nums[i] == nums[nums[i]-1]:
                    i += 1
                else:
                    nums[nums[i]-1] , nums[i] = nums[i] , nums[nums[i]-1]
            else:
                i += 1
        res = []
        for i,num in enumerate(nums):
            if i != num - 1:
                res.append(num)
                res.append(i + 1)
        return res