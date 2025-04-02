# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        left = 0
        n = len(citations)
        right = n-1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                ans = n - mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


