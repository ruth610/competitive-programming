# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def traverse(root):
            if not root:
                return 0
            count_t = 0
            if root.val % 2 ==0 :
                if root.left:
                    if root.left.left:
                        count_t += root.left.left.val
                    if root.left.right:
                        count_t += root.left.right.val
                if root.right:
                    if root.right.left:
                        count_t += root.right.left.val
                    if root.right.right:
                        count_t += root.right.right.val
            count_t += traverse(root.left)
            count_t += traverse(root.right)
            return count_t
        return traverse(root)




            
