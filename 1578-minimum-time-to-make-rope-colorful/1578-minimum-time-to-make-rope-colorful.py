class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        last_color, max_time, sum_time = '', 0, 0
        for c,t in zip(colors, neededTime):
            if c == last_color:
                max_time = max(t, max_time)
            else:
                sum_time += max_time
                last_color, max_time = c, t
        return sum(neededTime) - sum_time - max_time