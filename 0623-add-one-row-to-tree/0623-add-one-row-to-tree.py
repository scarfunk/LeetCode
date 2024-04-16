# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def DFS(node, dp, isL):
            
            if dp == depth :
                n = TreeNode(val)
                if isL:
                    n.left = node
                else:
                    n.right = node
                return n
            
            if node is None:
                return node
            
            node.left = DFS(node.left, dp+1, True)
            node.right = DFS(node.right, dp+1, False)
            return node
            
        return DFS(root, 1, True)
#         print(root)
        
#         return root