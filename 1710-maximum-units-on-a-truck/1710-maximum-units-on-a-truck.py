class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1],reverse= True)
        ans =0
        for x in boxTypes:
            if truckSize >= x[0]:
                ans += x[0]*x[1]
                truckSize-=x[0]
            elif truckSize < x[0]:
                ans+=truckSize * x[1]
                break
        return ans