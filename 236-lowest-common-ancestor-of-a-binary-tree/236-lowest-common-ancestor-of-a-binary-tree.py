# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = [None]
        def lca(node):
            if node==None:
                return False
            
            le = lca(node.left)
            ri = lca(node.right)
            
            mid = node==p or node==q
            # print(le,ri)
            if mid+le+ri>=2:
                ans[0] = node
            return mid or le or ri
        lca(root)
        return ans[0]
            
        