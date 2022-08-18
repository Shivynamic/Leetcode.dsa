from collections import defaultdict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = defaultdict(lambda:0)
        for i in arr:
            d[i]+=1
        
        a = []
        for i in d:
            a.append([i,d[i]])
        a.sort(key= lambda i:i[1],reverse=True)
        print(a)
        k=0
        count=0
        s = len(arr)//2
        for i in a:
            k+=i[1]
            count+=1
            print(k)
            if k>=s:
                return count
        
        