from functools import cache


class DFSSolution:
    """
    brutal force
    TC: O(2^(len1 + len2))
    SC: O(len1 + len2)
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.res = 0

        def dfs(t1, t2, commonLen):
            n = 0
            if len(t1) == 0 or len(t2) == 0:
                return
            if t1[0] == t2[0]:
                n += 1
                commonLen += 1
                self.res = max(self.res, commonLen)

            dfs(t1[1:], t2[n:], commonLen)
            dfs(t1[n:], t2[1:], commonLen)

        dfs(text1, text2, 0)
        return self.res


class DFSMemoSolution:
    """
    Error On LeetCode: "Memory Limit Exceeded"
    TC: O(len1 * len2)
    SC: O(len1 * len2)
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.res = 0

        @cache
        def dfs(t1, t2, commonLen):
            n = 0
            if len(t1) == 0 or len(t2) == 0:
                return
            if t1[0] == t2[0]:
                n += 1
                commonLen += 1
                self.res = max(self.res, commonLen)

            dfs(t1[1:], t2[n:], commonLen)
            dfs(t1[n:], t2[1:], commonLen)

        dfs(text1, text2, 0)
        return self.res


class DPSolution:
    """
    Bottom-up DP
    TC: O(len1 * len2)
    SC: O(len1 * len2)
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]  # NOTICE for the row-col
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # boundary is for checking the max value
        return dp[len1][len2]


print(DPSolution().longestCommonSubsequence("abcde", "ace"))
