import math
from functools import cache
from typing import List


class WrongDFSSolution:
    """
    NOTE: It's wrong because max(dfs(i, j + 1), dfs(i + 1, j)) will cause comflict for the same i, j pointer
    brutal force with dfs recurrsion
    """

    def maxProfit(self, prices: List[int], fee: int) -> int:

        def dfs(prices, fee, i, j, base, flag, res):
            if i >= len(prices) or j >= len(prices):
                return res

            if i < j:
                res = max(res, base + prices[j] - prices[i] - fee)
                flag = 0
            elif i > j and flag == 0:
                base += res
                flag = 1

            # print("i:", i, "j:", j, "base:", base, "res:", res, "fee:", fee)

            return max(dfs(prices, fee, i, j + 1, base, flag, res), dfs(prices, fee, i + 1, j, base, flag, res))

        return dfs(prices, fee, 0, 0, 0, 0, 0)


print(WrongDFSSolution().maxProfit([1, 3, 1, 4, 1, 5], 1))


class Solution:
    """
    Using Greedy Algorithm
    """
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell, buy = 0, -math.inf
        for price in prices:
            sell_tmp = sell
            sell = max(sell, buy + price - fee)
            buy = max(buy, sell_tmp - price)
            print("price:", price, "sell_tmp:", sell_tmp, "sell:", sell, "buy:", buy)
        return sell


print(Solution().maxProfit([1, 4, 6, 2, 8, 3, 10, 14], 3))
print(Solution().maxProfit([1, 2, 3, 15], 2))
