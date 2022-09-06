# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        def oone(node):
            if node==None:
                return False
            leftt = oone(node.left)
            rightt = oone(node.right)
            if not leftt:
                node.left = None
            if not rightt:
                node.right = None
            return node.val or leftt or rightt
        
        
        return root if oone(root) else None
    