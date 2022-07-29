def check(d1, w):
    d2 = defaultdict(lambda:0)
    for i in w:
        d2[i]+=1
    l1 = []
    l2 =[]
    for i in d1:
        l1.append(d1[i])
    for j in d2:
        l2.append(d2[j])
    return l1==l2

# def buildd(w):
#     d = defaultdict(lambda:0)
#     l = []
#     for i in w:
#         d[i]+=1
#         l.append(d[i])
#     return l

from collections import defaultdict
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True
        
        out = []
        
        for w in words:
            if match(w):
                out.append(w)
        return out
        
        
        
        
        
        
        
        
        #         out =[]
#         for i in words:
#             m1 ,m2 = {},{}
#             if len(i)!= len(pattern):
#                 continue
#             for j in range(len(pattern)):
#                 if i[j] not in m1:
#                     m1[i[j]] = pattern[j]
#                 if pattern[j] not in m2:
#                     m2[pattern[j]] = i[j]
#                 if (m1[i[j]],m2[pattern[j]])!= (pattern[j],i[j]) or len(set(pattern))!=len(set(i)):
#                     continue
#                 if j == len(pattern)-1 and (m1[i[j]],m2[pattern[j]])== (pattern[j],i[j]):
#                     out.append(i)
#         return out
                    
                    
        # l1 = buildd(pattern)
        # res = []
        # for w in words:
        #     if buildd(w)==l1:
        #         res.append(w)
        # return res
                
        
        # d1 = defaultdict(lambda:0)
        # for i in pattern:
        #     d1[i]+=1
        # o = []
        # for w in words:
        #     if check(d1,w):
        #         o.append(w)
        # return o