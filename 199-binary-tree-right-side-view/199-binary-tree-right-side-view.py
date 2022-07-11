# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
def levelorder(root):
    res = []
    q = collections.deque()
    q.append(root)
    
    while q:
        level =[]
        for i in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res
    
    
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out =[]
        a = levelorder(root)
        print(a)
        for i in a:
            # pass
            out.append(i[-1])
        return out