# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self,n):
        self.parent = [-1 for i in range(n+1)]
    def find(self,x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,a,b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        if root_a > root_b:
            root_a , root_b = root_b, root_a
        
        self.parent[root_a] += self.parent[root_b]
        self.parent[root_b] = root_a
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAccount = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAccount:
                    uf.union(emailToAccount[e],i)
                else:
                    emailToAccount[e] = i
        emailGroup = defaultdict(list)
        for e,i in emailToAccount.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        res = []
        for i,emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        return res

        