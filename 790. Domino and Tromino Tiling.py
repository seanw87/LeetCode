class Solution:
    def numTilings(self, n: int) -> int:
        modbase = 10e9 + 7
        dp = {1: 1, 2: 2, 3: 5}
        if n <= 3:
            return dp[n]
        for i in range(4, n+1):
            dp[i] = 2*dp[i-1] + dp[i-3]
            dp[i] %= modbase
            dp[i] = int(dp[i])

        return dp[n]