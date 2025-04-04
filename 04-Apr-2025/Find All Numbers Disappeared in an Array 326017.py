# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
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
                res.append(i + 1)
        return res