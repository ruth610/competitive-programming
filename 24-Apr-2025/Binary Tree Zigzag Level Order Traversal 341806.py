# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = 0
        q = deque([root])
        result = []
        while q:
            res = []
            size = len(q)
            for i in range(len(q)):
                val = q.popleft()
                res.append(val.val)
                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)
            if level % 2 ==1:
                l , r = 0 , len(res)-1
                while l < r:
                    res[l] , res[r] = res[r] , res[l]
                    l += 1
                    r -= 1
            result.append(res)
            level += 1
        return result