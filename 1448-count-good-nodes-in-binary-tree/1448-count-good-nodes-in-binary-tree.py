# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(node,maxx):
            
            if node== None:
                return 0
            
            if node.val>=maxx:
                res =1
            else:
                res =0
            maxx = max(maxx,node.val)
            res += helper(node.left,maxx)
            res += helper(node.right,maxx)
            return res
        
        return helper(root,root.val)