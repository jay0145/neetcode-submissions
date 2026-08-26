class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] <= low:
                low = prices[i]
            else:
                maxProfit = max(prices[i] - low, maxProfit)

        return maxProfit