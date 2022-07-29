class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minProfit = 999999999
        maxProfit =0
        for i in range(len(prices)):
            if prices[i]<minProfit:
                minProfit = prices[i]
            elif (prices[i]-minProfit)>maxProfit:
                maxProfit = prices[i] - minProfit
        return maxProfit
        