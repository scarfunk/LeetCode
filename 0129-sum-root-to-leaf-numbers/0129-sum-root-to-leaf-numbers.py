# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        global arr
        arr = []
        def dfs(node, prev):
            # print(node, prev)
            global arr
            prev = prev + str(node.val)
            if node.left is None and node.right is None:
                # print("apend")
                arr.append(prev)
                return
            if node.left: dfs(node.left, prev)
            if node.right: dfs(node.right, prev)
            
        dfs(root, "")
        # print(arr)
        res = sum([int(a) for a in arr])
        return res