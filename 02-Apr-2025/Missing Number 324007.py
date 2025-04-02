# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums=sorted(nums)
        newNums=set(nums)
        # for num in nums:
        #     if num!=0 and num-1 not in newNums:
        #         return num-1
        #     if num+1 not in newNums:
        #         return num+1
        for i in range(len(nums)+1):
            if i not in newNums:
                return i
                