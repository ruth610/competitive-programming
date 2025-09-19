# Problem: Next Permutation - https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # 1. Find the first decreasing index from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # 2. Find the element just larger than nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 3. Swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # 4. Reverse the suffix starting from i+1
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1