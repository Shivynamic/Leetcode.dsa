def consecutivee(arr):
    maxx= -1
    for i in range(len(arr)-1):
        maxx= max(maxx , (arr[i+1]-arr[i]))
    return maxx
    
        
        
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0,h])
        verticalCuts.extend([0,w])
        horizontalCuts.sort()
        verticalCuts.sort()
        ans = consecutivee(horizontalCuts) * consecutivee(verticalCuts)
        
        return ans% ((10**9)+7)