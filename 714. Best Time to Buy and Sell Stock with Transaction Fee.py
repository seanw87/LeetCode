import math
from functools import cache
from typing import List


class WrongDFSSolution:
    """
    NOTE: It's WRONG because max(dfs(i, j + 1), dfs(i + 1, j)) will cause comflict for the same i, j pointer
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


class DPSolution:
    """
    So here the senario is "buying" and "selling"(and implict "retain" action) the stock at "i"(th) day,
    and a "fee" when selling
    the result of the state matrix "dp" should be the max profit after "k" actions and the action of ith day
        the first state should be the day: i
        the second state should be the number of action pairs(buy and sell): k
        the third state should be whether the stock retained at the beginning of ith day, 1:retained, 0:NOT retained
    In conclusion: dp[i][k][0/1]
    The state machine is about the state changes after the ACTION:
        1. SELL: dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i] - fee)
        2. BUY: dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        The tricky thing: in BUY, the initial number of action pair when carrying out a BUY action should be "k-1"
    Initial state:
        dp[-1][k][0] = 0
        dp[-1][k][1] = -inf
        dp[i][0][0] = 0
        dp[i][0][1] = -info
    In this case:
        dp[i-1][k-1][0] == dp[i-1][k][0] == previous dp[i][k][0] because k can be infinit in this question
        so the state machine for this question would be:
        1. PREVIOUS STATE AFTER SELL: prev_sell = dp[i][k][0]
        2. SELL: dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i] - fee)
        3. BUY: dp[i][k][1] = max(dp[i-1][k][1], prev_sell - prices[i])
    """
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell, buy = 0, -math.inf
        for price in prices:
            sell_tmp = sell
            sell = max(sell, buy + price - fee)  # here sell and buy on the right are actually PREVIOUS sell and buy
            buy = max(buy, sell_tmp - price)  # here buy on the right is PREVIOUS buy
            print("price:", price, "sell_tmp:", sell_tmp, "sell:", sell, "buy:", buy)
        return sell


print(DPSolution().maxProfit([1, 4, 6, 2, 8, 3, 10, 14], 3))
print(DPSolution().maxProfit([1, 2, 3, 15], 2))
