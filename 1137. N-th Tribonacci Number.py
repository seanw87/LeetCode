class RecursionSolution:
    """
    recursion way
    """

    def tribonacci(self, n: int) -> int:
        existing = {}

        def dp(n):
            if n in (2, 1):
                existing[n] = 1
                return 1
            elif n == 0:
                existing[n] = 0
                return 0

            if n in existing:
                return existing[n]
            else:
                existing[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)

            return existing[n]

        return dp(n)


print(Solution().tribonacci(6))


class DPMatrixSolution:
    """
    DP Matrix
    """

    def tribonacci(self, n: int) -> int:
        dp = {0: 0, 1: 1, 2: 1}
        if n < 3:
            return dp[n]
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]
