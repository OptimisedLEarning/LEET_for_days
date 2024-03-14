class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
    
        min_price = prices[0]  # Initialize min_price to the price on the first day
        max_profit = 0
    
        for i in prices[1:]:
        # Update min_price if the current price is lower
            min_price = min(min_price, i)
        
        # Update max_profit if selling at the current price yields a higher profit
            max_profit = max(max_profit, i - min_price)
    
        return max_profit