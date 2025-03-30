# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        valid_nodes = 0
        def dfs(curr):
            nonlocal valid_nodes
            if not curr:
                return (0,0)
            n_left , left_sum = dfs(curr.left)
            n_right , right_sum = dfs(curr.right)

            n = 1 + n_left + n_right
            summ = curr.val + left_sum + right_sum

            avg = summ // n
            if curr.val == avg:
                valid_nodes += 1
            return (n,summ)
        dfs(root)
        return valid_nodes
         

            

