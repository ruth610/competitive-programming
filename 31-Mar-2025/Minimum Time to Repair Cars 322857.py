# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def answer(tot_min):
            total_cars = 0
            for n in ranks:
                b = tot_min // n
                ans = int(sqrt(b))
                total_cars += ans
            return total_cars
        l = 0
        r = 10**14
        result = 0
        while l <= r:
            mid = (r + l) // 2
            ans = answer(mid)
            if ans >= cars:
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result



