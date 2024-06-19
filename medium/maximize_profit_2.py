from typing import List

# class Solution:

#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         profits=[]
#         for i, cost_price in enumerate(prices):
#             # i wont buy and sell at the same day
#             for j in range(i+1,len(prices)):
#                 buy_day = i+1
#                 sell_day = j+1
#                 sale_price = prices[j]
#                 if sale_price < cost_price:
#                     continue
#                 profits.append({
#                     'buy_day':buy_day,
#                     'sell_day':sell_day,
#                     'profit':sale_price-cost_price,
#                 })

#         selected_profits = []
#         for profit_data in profits:
#             if profit_data
            
#         return 0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            current_price = prices[i]
            last_price = prices[i - 1]
            if current_price > last_price:
                profit += last_price - last_price
        return profit

print(Solution().maxProfit([7,1,5,3,6,4]))

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
