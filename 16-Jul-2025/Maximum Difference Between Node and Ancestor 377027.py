# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def recur(node,maxVal,minVal):
            if not node:
                # print(maxVal)
                return maxVal - minVal
            maxVal = max(maxVal , node.val)
            minVal = min(minVal , node.val)
            left = recur(node.left,maxVal,minVal) 
            right = recur(node.right,maxVal,minVal)
            return max(left , right)
        return recur(root, root.val,root.val)

