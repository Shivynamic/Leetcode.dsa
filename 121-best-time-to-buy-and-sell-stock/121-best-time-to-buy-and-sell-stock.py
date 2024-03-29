class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = 9999999999
        maxP = 0
        for i in range(len(prices)):
            if prices[i]<minP:
                minP = prices[i]
            elif (prices[i] - minP)>maxP:
                maxP = prices[i] - minP
        return maxP
