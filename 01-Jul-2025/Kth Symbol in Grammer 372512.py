# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n  == 1:
            return 0
        parent = self.kthGrammar(n - 1 , (k + 1) // 2)
        isKodd = k % 2 == 1
        if parent == 1:
            return 1 if isKodd else 0
        else:
            return 0 if isKodd else 1
        