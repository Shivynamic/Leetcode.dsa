class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def dfs(cur):
            
            if len(cur)==n:
                if len(cur)==1 or cur[0]!=0:
                    out.add(int(''.join([str(r) for r in cur])))
                return
            
            prev = cur[-1]
            
            if prev+k<=9:
                cur.append(prev+k)
                dfs(cur)
                cur.pop()
            
            if prev-k>=0:
                cur.append(prev-k)
                dfs(cur)
                cur.pop()
        
        out = set()
        
        for i in range(10):
            dfs([i])
        return list(out)