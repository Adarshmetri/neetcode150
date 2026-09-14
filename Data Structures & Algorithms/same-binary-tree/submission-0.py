# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        P = deque([p])
        Q = deque([q])

        while P or Q:
            node1 = P.popleft()
            node2 = Q.popleft()

            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False
            P.append(node1.left)
            P.append(node1.right)
            Q.append(node2.left)
            Q.append(node2.right)

        return True