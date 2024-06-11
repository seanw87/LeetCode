import math
from functools import cache
from itertools import product


class DFSSolution:
    """
    Brutal Force
    TC: O(2^(m+n))
    SC: O(m+n)
    """

    def uniquePaths(self, m: int, n: int) -> int:
        if m < 0 or n < 0:
            return 0
        if m == 1 and n == 1:
            return 1
        # print(m, n)
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


print(DFSSolution().uniquePaths(3, 7))


class DFSMemoSolution:
    """
    Store calculated result into a list
    TC: O(m*n)
    SC: O(m*n)
    """

    def uniquePaths(self, m: int, n: int) -> int:
        self.existed = [[-1] * (n + 1) for _ in range(m + 1)]

        def dp(m, n):
            if m < 0 or n < 0:
                return 0
            if m == 1 and n == 1:
                return 1
            if self.existed[m][n] != -1:
                return self.existed[m][n]

            self.existed[m][n] = dp(m - 1, n) + dp(m, n - 1)

            return self.existed[m][n]

        return dp(m, n)


print(DFSMemoSolution().uniquePaths(3, 7))


class DFSMemoUsingAnnotationSolution:
    """
    Using functools.cache
    """

    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(m, n):
            if m < 0 or n < 0:
                return 0
            if m == 1 and n == 1:
                return 1

            return dp(m - 1, n) + dp(m, n - 1)

        return dp(m, n)


class DPSolution:
    """
    Using state transition matrix
    TC: O(m*n)
    SC: O(m*n)
    """

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


class DPSCEfficientSolution:
    """
    current state is only associated with the previous two states.
    """

    def uniquePaths(self, m, n):
        dp = [1] * n
        for _, j in product(range(1, m), range(1, n)):
            dp[j] += dp[j - 1]
        return dp[-1]


print(DPSCEfficientSolution().uniquePaths(3, 7))
