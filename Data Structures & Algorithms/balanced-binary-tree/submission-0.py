# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.track = 0
        def dfs(node):   
            if not node:
                return 0 
            
            right = dfs(node.right)
            left = dfs(node.left)

            if abs(right - left) > 1:
                self.track = 1
            return 1 + max(right, left)

        dfs(root)
        if self.track == 0:
            return True
        else:
            return False