# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        boat=0
        while l<=r:
            if people[l]+people[r]<=limit:
                boat+=1
                r-=1
                l+=1
            else:
                boat+=1
                r-=1
        return boat
