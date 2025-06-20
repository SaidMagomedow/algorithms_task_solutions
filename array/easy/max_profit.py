# task - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:

    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        # prices = [7,1,5,3,6,4] | [7,6,4,3,1] | [3,2,6,5,0,3]
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

print(Solution.maxProfit(prices=[3,2,6,5,0,3]))