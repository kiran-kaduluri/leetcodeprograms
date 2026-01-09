# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (0, None)

            lh, ln = dfs(node.left)
            rh, rn = dfs(node.right)

            if lh > rh:
                return (lh + 1, ln)
            elif rh > lh:
                return (rh + 1, rn)
            else:
                return (lh + 1, node)
                
        return dfs(root)[1]

        