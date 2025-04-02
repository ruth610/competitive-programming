# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        def isGood(target):

            for house in houses:

                left , right = 0 , len(heaters)-1

                while left <= right:

                    mid = (left + right) // 2
                    if heaters[mid] < house - target:
                        left = mid + 1
                    else:
                        right = mid - 1

                    if left < len(heaters) and heaters[left] <= target + house:
                        continue

                    return False

            return True
            
        left = 0
        right = max(max(houses),max(heaters)) - min(min(houses),min(heaters))
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if isGood(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

            
                
