from typing import List


class RecursiveInefficientSolution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)

        def dp(k):
            if k < 0:
                return 0

            return max((dp(k - 2) + nums[k]), dp(k - 1))  # adjacent element cannot be merged

        dp(n - 1)


class RecursiveMemoSolution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        existed = [-1] * n

        def dp(k):
            if k < 0:
                return 0

            if existed[k] != -1:
                return existed[k]
            existed[k] = max((dp(k - 2) + nums[k]), dp(k - 1))  # adjacent element cannot be merged

            return existed[k]

        return dp(n - 1)


class DPSolution:
    """
    SC: O(n)
    """

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = {}

        for i in range(n + 1):
            if i == 0:
                dp[i] = 0  # offset dp to left
            elif i == 1:
                dp[i] = nums[0]
            else:
                dp[i] = max((dp[i - 2] + nums[i - 1]), dp[i - 1])

        return dp[n]


print(DPSolution().rob([2, 1, 1, 2]))


class DPMostEfficientSolution:
    """
    SC: O(1)
    order: prev2, prev1, num
    """

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev1, prev2 = 0, 0
        for num in nums:
            tmp = prev1
            prev1 = max((prev2 + num), prev1)
            prev2 = tmp
        return prev1

