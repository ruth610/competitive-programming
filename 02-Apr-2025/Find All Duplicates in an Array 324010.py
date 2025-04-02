# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count_num=Counter(nums)
        res=[]
        for n in count_num:
            if count_num[n]>1:
                res.append(n)
        return res
