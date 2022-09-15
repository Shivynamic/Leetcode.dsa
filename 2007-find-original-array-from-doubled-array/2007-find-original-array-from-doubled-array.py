class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        ans = []
        
        smaller = collections.Counter()
        for x in changed:
            if x%2==0 and x//2 in smaller and smaller[x//2] >0:
                ans.append(x//2)
                smaller[x//2]-=1
            else:
                smaller[x] +=1
        
        if len(ans)*2 != len(changed):
            return []
        return ans
        
        
        '''if len(changed)%2==1:
            return []
        changed.sort()
        for i in range(len(changed)):
            a = 2*changed[i]
            if a==0:
                if 0 in changed[i+1:]:
                    # print("in",changed)
                    p = changed[i+1:].index(0)
                    # print(p)
                    changed[i+p+1]=-1
                else:
                    changed[i]=-1
            elif a in changed:
                t = changed.index(a)
                changed[t] = -1
            elif a not in changed:
                changed[i]=-1
            # print(changed)
            
        res = []
        for i in changed:
            if i!=-1:
                res.append(i)
        if len(res)!=(len(changed)/2):
            return []
        return res'''