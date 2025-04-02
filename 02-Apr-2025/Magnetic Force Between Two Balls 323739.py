# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def isPostionPossible(target):
            last = position[0]
            count = 1
            for i in range(1,len(position)):
                if position[i] - last >= target:
                    last = position[i]
                    count += 1
                    if count >= m:
                        return True
            return count >= m
        
        left = 1
        right = max(position)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if isPostionPossible(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
        
