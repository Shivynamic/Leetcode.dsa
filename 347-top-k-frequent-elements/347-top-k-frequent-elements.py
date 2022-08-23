class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.defaultdict(lambda:0)
        
        for i in nums:
            d[i]+=1
        
        freq = [[] for i in range(len(nums)+1)]
        
        for i in d:
            freq[d[i]].append(i)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res