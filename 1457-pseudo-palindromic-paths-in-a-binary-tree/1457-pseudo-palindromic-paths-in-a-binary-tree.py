# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans =0 
        def search(node,even):
            if node is None:
                return
            
            even[node.val] = not even[node.val]
            
            if node.left is None and node.right is None:
                if sum(even)<=1:
                    nonlocal ans
                    ans+=1
            else:
                search(node.left,even)
                search(node.right,even)
            
            even[node.val] = not even[node.val]
        search(root,[False]*10)
        return ans
                
            
        
        
        
        '''def isPalindrome(l):
            c = Counter(l)
            
            one = False
            for k,v in c.items():
                if v%2!=0:
                    if one:
                        return False
                    else:
                        one= True
            return True
        
        def dfs(node,path):
            if not node:
                return 0
            
            elif not node.left and not node.right:
                if isPalindrome(path+[node.val]):
                    return 1
                else:
                    return 0
                
            return dfs(node.left,path+[node.val])+dfs(node.right,path+[node.val])
        
        return dfs(root,[])'''