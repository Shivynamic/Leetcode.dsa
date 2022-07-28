from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1= defaultdict(lambda:0)
        d2 = defaultdict(lambda:0)
        for i in s:
            d1[i]+=1
        for i in t:
            d2[i]+=1
        print(d1,d2)
        return d1==d2