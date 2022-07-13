# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                node =q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        ans=[]
        q=collections.deque()
        q.append(root)
        while q:
            ql=len(q)
            a=[]
            for i in range(ql):
                node=q.popleft()
                if node:
                    a.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if a:
                ans.append(a)
        return ans
'''
        # ans = []
        # q = collections.deque()
        # q.append(root)
        # while q:
        #     q1 = len(q)
        #     a = []
        #     for i in range(q1):
        #         node = q.popleft()
        #         if node:
        #             a.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #     if a:
        #         ans.append(a)
        # return ans
        