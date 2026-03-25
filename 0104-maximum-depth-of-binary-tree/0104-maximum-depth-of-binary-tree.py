# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    depth=0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node,d):

            if not node:
                return
            dfs(node.left,d+1)
            dfs(node.right,d+1)
            if d>self.depth:
                self.depth=d
        dfs(root,1)
        return self.depth
