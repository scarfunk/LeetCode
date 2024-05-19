# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.move = 0
        def dfs(node):
            if node is None: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.move += abs(left) + abs(right)
            
            return node.val + left + right -1
                    
        dfs(root)
        print(self.move)
        return self.move