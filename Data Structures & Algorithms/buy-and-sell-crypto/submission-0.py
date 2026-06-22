class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        i=0
        while i < len(prices):
            j = i+1
            while j < len(prices):
                profit = prices[j]-prices[i]
                max_profit = max(profit, max_profit)
                j+=1
            i+=1
        
        return max_profit

            
