class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n,m = len(target),len(stamp)
        output=[]
        
        move,maxmoves=0,10*n
        premove =0
        
        def check(src,trg):
            works = False
            for i in range(m):
                if src[i]==trg[i]:
                    works = True
                elif src[i]=="?":
                    continue
                else:
                    return False
            return works
        
        while move<maxmoves:
            premove = move
            for i in range(n-m+1):
                if check(target[i:i+m],stamp):
                    move+=1
                    output.append(i)
                    target = target[:i]+("?"*m)+target[i+m:]
                    if target=="?"*n:
                        return reversed(output)
            if premove==move:
                return []