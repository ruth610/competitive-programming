# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        col = len(isConnected[0])
        cityConnection = defaultdict(list)
        for i,city in enumerate(isConnected):
            for j in range(len(city)):
                if i != j and city[j]:
                    cityConnection[i].append(j)
            if not cityConnection[i]:
                cityConnection[i] = []
        # print(cityConnection)
        visited = set()
        def dfs(city):
            cities = cityConnection[city]
            visited.add(city)
            for i in cities:
                if i not in visited:
                    dfs(i)
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                count += 1
        return count