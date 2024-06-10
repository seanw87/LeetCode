from typing import List
import math


class InefficientDFSSolution:
    """
    Won't pass the case because of full tree search
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0

        start = -1

        def dp(k, res):
            if k >= len(cost):
                return res

            if k >= 0:
                res += cost[k]

            return min(dp(k + 1, res), dp(k + 2, res))

        return dp(start, 0)


print(InefficientDFSSolution().minCostClimbingStairs([10, 15, 20]))


class EfficientDFSSolution:
    """
    Solve: Add memory (exchange time with space)
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0

        n = len(cost)
        existed = [-1] * n

        def dp(k):
            if k < 0: return 0
            if k in (0, 1): return cost[k]
            if existed[k] != -1:
                return existed[k]
            existed[k] = cost[k] + min(dp(k - 1), dp(k - 2))
            return existed[k]

        return min(dp(n - 1), dp(n - 2))


print(EfficientDFSSolution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))


class DPSolution:
    """
    Using status transfer matrix
    SC: O(n)
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        n = len(cost)

        dp = {}

        for i in range(n):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[n - 1], dp[n - 2])


class EfficientDPSolution:
    """
    SC: O(1)
    """

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        n = len(cost)
        first = cost[0]
        second = cost[1]
        if n <= 2: return min(first, second)
        for i in range(2, n):
            curr = cost[i] + min(first, second)
            first = second
            second = curr

        return min(first, second)
