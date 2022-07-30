def check(w,d):
    d1 = defaultdict(lambda:0)
    for i in w:
        d1[i]+=1
    
    for x in d:
        if x not in d1 or d[x]>d1[x]:
            return False
        
    return True

 


from collections import defaultdict
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        d = defaultdict(lambda:0)
        for i in words2:
            for j in i:
                if j not in d:
                    d[j] = i.count(j)
                else:
                    d[j] = max(d[j], i.count(j))
        out = []
        for w in words1:
            if check(w,d):
                out.append(w)
        return out

# def check(w,d):
#     d1 = defaultdict(lambda:0)
#     for i in w:
#         d1[i]+=1
    
#     for x in d:
#         if x not in d1 or d[x]>d1[x]:
#             return False
        
#     return True

 


# from collections import defaultdict
# class Solution:
#     def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
#         d = defaultdict(lambda:0)
#         for i in words2:
#             for j in i:
#                 if j not in d:
#                     d[j] = i.count(j)
#                 else:
#                     d[j] = max(d[j], i.count(j))
#         out = []
#         for w in words1:
#             if check(w,d):
#                 out.append(w)
#         return out
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        out = []
        for w in words1:
            if checkk(w,words2):
                out.append(w)
        return out
        '''
                
        #         a = "".join(words2)
#         print(a)
#         d =defaultdict(lambda:0)
#         for i in a:
#             d[i]+=1
#         print(d)
#         out = []
        
#         for w in words1:
#             if check(w,d):
#                 out.append(w)
#         return out
        