class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        out = [intervals[0]]
        
        for s,e in intervals[1:]:
            last = out[-1][1]
            if s<= last:
                out[-1][1] = max(last,e)
            else:
                out.append([s,e])
        return out