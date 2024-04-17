# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        tmp = []
        def DFS(node, agg):
            agg = chr(node.val + 97) + agg
            if node.left is None and node.right is None:
                tmp.append(agg)
                return
            # chr(97) => "a"
            if node.left: DFS(node.left, agg)
            if node.right: DFS(node.right, agg)
            
            
        
        DFS(root, "")
        tmp.sort()
        print(tmp)
        return tmp[0]
        
            
            
            
            