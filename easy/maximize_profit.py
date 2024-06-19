from typing import List

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         for i, buy_price in enumerate(prices):
#             for j in range(i,len(prices)):
#                 sale_price=prices[j]
#                 profit=sale_price - buy_price  
#                 if profit > max_profit:
#                     max_profit=profit
#         return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        buy_price = prices[0]
        max_profit = 0
        for sale_price in prices:
            if sale_price < buy_price:
                buy_price = sale_price
            profit = sale_price - buy_price
            if profit>max_profit:
                max_profit = profit
        return max_profit

prices = [1,2]
print(Solution().maxProfit(prices))


