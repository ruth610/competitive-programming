# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        for trusts,trusted in trust:
            indegree[trusts] += 1
            outdegree[trusted] += 1
        for i in range(1, n+1):
            if outdegree[i] == n - 1 and indegree[i] == 0:
                return i
        return -1


       

