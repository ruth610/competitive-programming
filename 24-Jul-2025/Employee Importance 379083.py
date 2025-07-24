# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.lookUp = {employee.id:employee for employee in employees}
        def dfs(id):
            subordinateId = self.lookUp[id].subordinates
            total = self.lookUp[id].importance
            if subordinateId:
                for j in subordinateId:
                    total += dfs(j)
            return total
        return dfs(id)
        
                    
            