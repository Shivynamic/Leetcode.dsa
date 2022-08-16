class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append([startTime[i],endTime[i],profit[i]])
        
        jobs.sort(key = lambda i:i[0])
        heap = []
        mp,cp =0,0
        for s,e,p in jobs:
            while heap and heap[0][0]<=s:
                et,tmp = heapq.heappop(heap)
                cp = max(cp,tmp)
            
            heapq.heappush(heap,(e,cp+p))
            mp = max(mp,cp+p)
        return mp
                