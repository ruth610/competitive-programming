# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def howManyDays(capacity):
            tot_days = 1
            curr_sum = 0
            for i in range(len(weights)):
                if curr_sum + weights[i] <= capacity:
                    curr_sum += weights[i]
                    
                else:
                    curr_sum = weights[i]
                    tot_days += 1
                    
            return tot_days <= days 

        l = max(weights)
        r = sum(weights)
        result = 0
        while l <= r:
            mid = (l + r) // 2
            ans = howManyDays(mid)
            if ans:
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result